from django import forms
from .validators import validate_file, validate_file_size

choices = (('', 'Applying In'), ('backend', 'Backend'), ('mobile', 'Mobile'))


class InfoForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=256,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        required=True)
    email = forms.EmailField(
        label='',
        max_length=256,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        required=True)

    phone = forms.CharField(
        label='',
        max_length=14,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
        required=True)

    full_address = forms.CharField(
        label='',
        max_length=512,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
        required=False)

    name_of_university = forms.CharField(
        label='',
        max_length=256,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'University'}),
        required=True)

    graduation_year = forms.IntegerField(
        label='',
        min_value=2015,
        max_value=2020,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Graduation Year'}),
        required=True)

    cgpa = forms.DecimalField(
        label='',
        max_digits=3,
        decimal_places=2,
        min_value=2,
        max_value=4,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'CGPA', 'step': .01}),
        required=False)

    experience_in_months = forms.IntegerField(
        label='',
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Experience in Months'}),
        required=False)

    current_work_place_name = forms.CharField(
        label='',
        max_length=256,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Current Work Place'}),
        required=False)

    applying_in = forms.ChoiceField(
        label='',
        choices=choices,
        required=True,
        widget=forms.Select(choices=choices, attrs={'class': 'form-control'}),

    )
    expected_salary = forms.IntegerField(
        label='',
        min_value=15000,
        max_value=60000,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Expected Salary'}),
        required=True)
    field_buzz_reference = forms.CharField(
        label='',
        max_length=256,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Field Buzz Reference'}),
        required=False)

    github_project_url = forms.URLField(
        label='',
        max_length=512,
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Github Project URL'}),
        required=True)

    file = forms.FileField(
        label='Upload your CV',
        validators=[validate_file, validate_file_size],
        widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'file'})
    )
