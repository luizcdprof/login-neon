from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.usuario_login, name='usuario_login'),
    path('cadastrar/', views.usuario_cadastrar, name='usuario_cadastrar'),
]