from django.urls import path
from . import views


app_name = 'balti'
urlpatterns = [
    path('', views.home, name='home'),
    path('balta-<str:balta_name>', views.detail, name='detail'),
    path('despre', views.about, name='about'),
    path('contact', views.contact, name='contact')
]
