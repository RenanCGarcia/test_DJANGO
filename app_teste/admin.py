from django.contrib import admin
from .models import BancoDados # Importa sua classe de criação do banco de dados
# Register your models here.
admin.site.register(BancoDados) # E registra ela no admin