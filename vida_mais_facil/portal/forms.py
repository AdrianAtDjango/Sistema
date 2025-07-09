from django import forms
from .models import *

class CadastraUser(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'cpf',
            'password',
            'p_nome',
            'sobrenome',
            'sexo',
            'foto_perfil',
            'rua',
            'numero',
            'bairro',
        ]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class CadastraSaude(forms.ModelForm):
    class Meta:
        model = RegistroSaude
        fields = [
            'f_cardiaca',
            'glicemia',
            'peso',
            'p_sistolica',
            'p_diastolica'
        ]

class LoginForm(forms.Form):
    cpf = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = [
            'medico',
            'especialidade',
            'titulo',
            'observacao',
            'emergencia',
            'status',
            'data_agendamento',
            'hora_agendamento',
        ]


"""
solicitante = models.ForeignKey(User, on_delete=models.CASCADE)
    medico = models.CharField(choices=MEDICO)
    especialidade = models.CharField(choices=ESPECIALIDADE, null=True, blank=True)
    titulo = models.CharField(max_length=255)
    observacao = models.TextField(null=True, blank=True)
    emergencia = models.CharField(choices=EMERGENCIA, default='Baixa')
    status =  models.CharField(choices=STATUS, default='Solicitado')
    data_solicitacao = models.DateField(auto_now=True)
    data_agendamento = models.DateField()
    hora_agendamento = models.CharField(choices=HORA)


"""