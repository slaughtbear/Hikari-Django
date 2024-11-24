from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('prueba/', views.prueba, name='prueba'),
]