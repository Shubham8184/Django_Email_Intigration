from django.urls import path
from .views import Emailsendview, Homeview


urlpatterns=[
    path('email/',Emailsendview,name='email'),
    path('home/',Homeview,name='home')
]
