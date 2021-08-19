from django.shortcuts import render, redirect
from .forms import InfoForm
import requests, time, uuid, json


def login(request):
    if request.method != 'POST':
        return render(request, 'login.html', {'invalid': False})

    username = request.POST.get('username')
    password = request.POST.get('password')

    URL = 'https://recruitment.fisdev.com/api/login/'
    res = requests.post(url=URL, json={'username': username, 'password': password})

    if not res.json()['success']:
        return render(request, 'login.html', {'invalid': True})
    else:
        request.session['token'] = res.json()['token'];
        return redirect('info')


def submit_info(request):
    if 'token' not in request.session:
        return redirect('login')

    if request.method != 'POST':
        form = InfoForm()
        return render(request, 'info.html', {'form': form})
    else:
        form = InfoForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            context = {}
            for key, value in data.items():
                if key == 'file':
                    continue
                if value != "":
                    context[key] = value

            context['tsync_id'] = str(uuid.uuid1())
            context['cv_file'] = {"tsync_id": str(uuid.uuid1())}
            context['on_spot_update_time'] = int(time.time() * 1000)
            context['cgpa'] = float(context['cgpa'])

            token = request.session['token']
            head = {'Authorization': 'token {}'.format(token)}

            URL = 'https://recruitment.fisdev.com/api/v1/recruiting-entities/'
            # URL = 'https://recruitment.fisdev.com/api/v0/recruiting-entities/'
            res = requests.post(url=URL, json=context, headers=head)

            if res.json()['success']:

                cv_id = res.json()['cv_file']['id']
                URL = 'https://recruitment.fisdev.com/api/file-object/' + str(cv_id) + '/'
                file = {'file': data['file'].read()}
                res = requests.put(URL, files=file, headers=head)

                if res.json()['success']:
                    request.session['success'] = True;
                    return redirect('success')

        return render(request, 'info.html', {'form': form})


def success(request):
    if 'token' not in request.session:
        return redirect('login')

    if 'success' not in request.session:
        return redirect('info')

    return render(request, 'success.html')


def logout(request):
    try:
        del request.session['token']
        del request.session['success']
    except KeyError:
        pass
    return redirect('login')
