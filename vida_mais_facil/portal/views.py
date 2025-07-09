from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .models import *
from .forms import *
from .utils import autentica_manual

def cadastra_user(request):
    if request.method == 'POST':
        form = CadastraUser(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('cadastra-saude')
    else:
        form = CadastraUser()

    context = {'form': form}
    return render(request, 'cadastra-user.html', context)

def cadastra_saude(request):
    if request.method == 'POST':
        form = CadastraSaude(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CadastraSaude()

    context = {'form': form}
    return render(request, 'cadastra-saude.html', context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            password = form.cleaned_data['password']
            user = autentica_manual(cpf, password)
            if user:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "CPF ou Senha Inválidos!")
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'login.html', context)

def dashboard(request):
    atendimentos = Atendimento.objects.all()
    context = {'atendimentos': atendimentos}
    return render(request, 'dashboard.html', context)

def visualizar_saude(request):
    registros = RegistroSaude.objects.all()
    context = {'registros': registros}
    return render(request, 'saude.html', context)

def nova_consulta(request):
    form = AtendimentoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {'form': form}
    return render(request, 'nova_consulta.html', context)

def deletar_consulta(request, id):
    atendimento = get_object_or_404(Atendimento, id=id)
    if request.method == 'POST':
        atendimento.delete()
        return redirect('dashboard')

    context = {'atendimento': atendimento}
    return render(request, 'deleta_consulta.html', context)

def editar_consulta(request, id):
    atendimento = get_object_or_404(Atendimento, id=id)
    if request.method == 'POST':
        form = AtendimentoForm(request.POST, instance=atendimento)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AtendimentoForm(instance=atendimento)
    
    context = {'form': form}
    return render(request, 'nova_consulta.html', context)
