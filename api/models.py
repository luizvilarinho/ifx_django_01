from django.db import models


class DbUModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=180)
    author = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.title


class Course(models.Model):
    description = models.CharField(max_length=180)
    time = models.CharField(max_length=100)
    school = models.CharField(max_length=180)

    def __str__(self):
        return self.description

