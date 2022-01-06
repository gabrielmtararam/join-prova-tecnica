from django.db import models
from datetime import datetime


class Cargos (models.Model):
    nome_cargo = models.CharField(
        verbose_name="Nome",
        max_length=100,
        db_column='nome_cargo',
    )

    class Meta:
        db_table = "Cargos"

class Pessoas (models.Model):
    nome = models.CharField(
        verbose_name="Nome ",
        max_length=200,
        db_column='nome',
    )
    admissao = models.DateField(
        default=datetime.now,
        verbose_name="Admissao",
        db_column='admissao',
    )
    cargo = models.ForeignKey(
        Cargos,
        db_column='id_cargo',
        on_delete=models.CASCADE, #pensar se excluo em cascata mesmo
        null= True,
    )
    class Meta:
        db_table = "Pessoas"

    def __str__(self):
        return str(self.id) + " "+str(self.nome) +" "+ str(self.admissao)+" "+str(self.cargo.nome_cargo)