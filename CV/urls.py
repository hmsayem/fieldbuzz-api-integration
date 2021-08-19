from django.urls import path
from .views import submit_info, login, success, logout

urlpatterns = [
    path('', login, name='login'),
    path('info/', submit_info, name='info'),
    path('success/', success, name='success'),
    path('logout/', logout, name='logout'),
]
