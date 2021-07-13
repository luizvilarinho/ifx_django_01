from django.db import models


class DbDModel(models.Model):
    DEPARTAMENTOS_CHOICES = [
        ('d1', 'Departamento 1'),
        ('d2', 'Departamento2'),
        ('d3', 'Departamento3'),
    ]

    departamento = models.CharField(max_length=2, choices=DEPARTAMENTOS_CHOICES)

    def __str__(self):
        return self.departamento
