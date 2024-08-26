from django.urls import path
from App.views import about, main, contacts

urlpatterns = [
    path('', about, name='home'),
    path('pages/about/', about, name='about'),
    path('pages/main/', main, name='main'),
    path('pages/contacts/', contacts, name='contacts'),
]
