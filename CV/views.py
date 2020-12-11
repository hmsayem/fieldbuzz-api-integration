from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import InfoForm
import requests, time, uuid

auth_token = "";

def login_view(request):
    if request.method != 'POST':
        return render(request, 'login.html', {"invalid": False})

    username = request.POST.get('username')
    password = request.POST.get('password')

    URL = "https://recruitment.fisdev.com/api/login/"
    res = requests.post(url=URL, json={"username": username, "password": password})

    if not res.json()["success"]:
        return render(request, 'login.html', {"invalid": True})
    else:
        global auth_token
        auth_token = res.json()["token"];
        return HttpResponseRedirect('info')


def submit_info(request):
    if request.method != 'POST':
        form = InfoForm()
        return render(request, 'info.html', {'form': form})
    else:
        form = InfoForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            context = {}
            for key, value in data.items():
                if key == "file":
                    continue
                if value != "":
                    context[key] = value

            context["tsync_id"] = str(uuid.uuid1())
            context["cv_file"] = {"tsync_id": str(uuid.uuid1())}
            context["on_spot_update_time"] = int(time.time() * 1000)
            context["cgpa"] = float(context["cgpa"])

            URL = "https://recruitment.fisdev.com/api/v0/recruiting-entities/"
            head = {'Authorization': 'token {}'.format(auth_token)}
            res = requests.post(url=URL, json=context, headers=head)

            cv_id = res.json()["cv_file"]["id"]
            URL = 'https://recruitment.fisdev.com/api/file-object/' + str(cv_id) + '/'
            file = {'file': data['file'].read()}
            res = requests.put(URL, files=file, headers=head)
            if res.json()["success"]:
                return render(request, 'success.html')

        return render(request, 'info.html', {'form': form})
