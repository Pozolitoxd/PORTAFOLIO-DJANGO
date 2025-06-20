from django.urls import path
from . import views
urlpatterns =[
    path('',views.inicio,name='inicio'),
    path('proyecto/',views.proyecto,name='proyecto'),
    path('contacto/',views.contacto,name='contacto')
]