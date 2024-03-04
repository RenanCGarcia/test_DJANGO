from django.db import models

# Criando a classe do Banco de dados, herdando a biblioteca models, de django.db
# Essa biblioteca "models" é a que entra em contato com o banco de dados.
class BancoDados(models.Model):
    # Agora precisamos criar os campos do nosso banco de dados
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    vivo = models.BooleanField(default=True)
    # O DJANGO cria a chave primária ID automaticamente

    # Essa função retorna as informações do Banco em string
    def __str__(self):
        return self.nome




# Temos vários tipos de campos
'''
IntegerField()                                              | Armazena valores inteiros (1)
FloatField()                                                | Armazena valores flutuantes (1.5)
CharField( max_length=numero, * )                           | Armazena texto com caracteres limitados pelo "max_length"
TextField()                                                 | Um grande campo de texto
DateField( auto_now=False , auto_now_add=False , * )        | Armazeta data, auto_now= define automaticamente a data para atual
TimeField( auto_now=False , auto_now_add=False , * )        | Armazena Tempo, auto_now= define automaticamente a data para atual
DateTimeField( auto_now=False , auto_now_add=False , * )    | Armazena Data e Tempo, auto_now= define automaticamente a data para atual
BooleanField()                                              | Armazena valores verdadeiros ou falsos
EmailField( max_length=254 , * )                            | Verifica se o email é válido
FileField( upload_to=None , max_length=100 , * )            | upload_to= caminho para salvar o arquivo
ImageField( upload_to=None , height_field=None , width_field=None , max_length=100 , * )
'''
