from django.db import models
from sex.models import Sex
from type.models import Type


class People(models.Model,):
    nome = models.CharField(max_length=200)
    type_blood = models.ForeignKey(Type, on_delete=models.PROTECT, related_name='type_blood')
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    sex = models.ForeignKey(Sex, on_delete=models.PROTECT, related_name='sex')

    def __str__(self):
        return self.nome
