from django.urls import path
from .views import submit_info, login_view
urlpatterns = [
    path('', login_view, name='login'),
    path('info/', submit_info, name='info'),
    path('success/', submit_info, name='success'),
]
