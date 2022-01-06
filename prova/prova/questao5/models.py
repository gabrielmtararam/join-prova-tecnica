from django.db import models

# Create your models here.
class registro_inmetro (models.Model):
    value = models.IntegerField(blank=True, null=True)

class Editora(models.Model):
    value = models.IntegerField(blank=True, null=True)

class Edicao(models.Model):
    value = models.IntegerField(blank=True, null=True)

class Livro(models.Model):
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    #One to Many
    edicoes = models.ManyToManyField(Edicao)
    registro_inmetro = models.OneToOneField(registro_inmetro, on_delete=models.CASCADE)
    #basicamente foreign key porem com unique=True
