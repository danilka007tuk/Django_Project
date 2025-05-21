from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('sfera/', views.sfera, name='sfera'),
    path('contact/', views.contact, name='contact')
]