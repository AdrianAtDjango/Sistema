from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastra_user, name='cadastra-user'),
    path('cadastrasaude/', views.cadastra_saude, name='cadastra-saude'),
    path('login/', views.login_user, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('novo/', views.nova_consulta, name='nova-consulta')
]