# #!/bin/bash

sleep 5
# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput
# Apply database migrations6
echo "Apply database migrations"
python manage.py migrate --fake-initialmigrate --fake-initial
python manage.py makemigrations
python manage.py migrate

# cria super usuario
echo "Cria super usuario"
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('sccp_app','sccp@sccorinthians.com.br', '@sccp123')"
python manage.py drf_create_token sccp_app

echo "######## criar grupo ###########"
python manage.py shell -c "from django.contrib.auth.models import User; from django.contrib.auth.models import Group; grupo_sccp_usuario = Group.objects.create(name='Usuario'); grupo_sccp_admin = Group.objects.create(name='Admin'); usuario = User.objects.get(username='sccp_app'); usuario.groups.add(grupo_sccp_admin)"

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000