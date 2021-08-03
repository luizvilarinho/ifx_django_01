#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import subprocess
import urllib
import time
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SCCP_APP.settings')

def _setup():
    # ''' Realiza o Setup do ambiente'''
    time.sleep(15)
    try:
        # #Realiza a instalação das bibliotecas
        # subprocess.run(["pip", "install","-r", "/webapps/requirements.txt"])
        #Realiza a migração do banco
        subprocess.run(["python3", "manage.py", "migrate", "--fake-initial"])
        subprocess.run(["python", "manage.py", "makemigrations"])
        subprocess.run(["python", "manage.py", "migrate"])
        #Resgata os Statics
        # subprocess.run(["python", "manage.py", "collectstatic"])
        #Cria superuser
        subprocess.run(["python", "manage.py", "shell", "-c", "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('sccp','carlos.fernandes@sccorinthians.com.br', '@sccp123')"])

        print('Processo concluído com sucesso')

    except Exception as e:
        print(e)

if __name__ == '__main__':
    _setup()