from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class RegistroSaude(models.Model):
    data_registro = models.DateTimeField(auto_now=True)
    f_cardiaca = models.IntegerField(verbose_name='Frequência Cardíaca', blank=True, null=True)
    glicemia = models.IntegerField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    p_sistolica = models.IntegerField(blank=True, null=True, verbose_name='Pressão Sistolica')
    p_diastolica = models.IntegerField(blank=True, null=True, verbose_name='Pressão Diastolica')

class User(AbstractBaseUser):
    SEX = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('outro', 'Outro'),
    ]

    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    # Campo 'Password' já vem por padrão
    p_nome = models.CharField(max_length=64, verbose_name='Primeiro Nome')
    sobrenome = models.CharField(max_length=64)
    sexo = models.CharField(choices=SEX)
    foto_perfil = models.ImageField(upload_to='perfis/', default='default.jpg')
    saude = models.ForeignKey(RegistroSaude, on_delete=models.CASCADE, blank=True, null=True)
    rua = models.CharField(max_length=255)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=255)
    
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['p_nome']

class Atendimento(models.Model):
    EMERGENCIA = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ]

    STATUS = [
        ('solicitado', 'Solicitado'),
        ('concluido', 'Concluido'),
    ]

    HORA = [
        ('08:00', '08:00'),
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
    ]

    MEDICO = [
        ('dr-joao', 'Dr. João Silva'),
        ('dra-maria', 'Dra. Maria Santos'),
        ('dr-pedro', 'Dr. Pedro Costa'),
        ('dra-ana', 'Dra. Ana Lima')
    ]

    ESPECIALIDADE = [
        ('cardiologia', 'Cardiologia'),
        ('geriatria', 'Geriatria'),
        ('clinicogeral', 'Clínico Geral'),
        ('oftalmologia', 'Oftalmologia'),
    ]
    
    medico = models.CharField(choices=MEDICO)
    especialidade = models.CharField(choices=ESPECIALIDADE, null=True, blank=True)
    titulo = models.CharField(max_length=255)
    observacao = models.TextField(null=True, blank=True)
    emergencia = models.CharField(choices=EMERGENCIA, default='Baixa')
    status =  models.CharField(choices=STATUS, default='Solicitado')
    data_solicitacao = models.DateField(auto_now=True)
    data_agendamento = models.DateField()
    hora_agendamento = models.CharField(choices=HORA)
