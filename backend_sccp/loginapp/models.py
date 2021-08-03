from django.db import models

# Create your models here.

class loginApp(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=False, null=False)
    passwd = models.TextField(blank=False, null=False)

    def __str__(self):
        return  id

    class Meta:
        db_table = 'useraccess'