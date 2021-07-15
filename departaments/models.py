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


class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    departament = models.ForeignKey(DbDModel, on_delete=models.CASCADE)
    email = models.EmailField()
    birth_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=250)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
