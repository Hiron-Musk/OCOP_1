import django
django.setup()

from django.db import models
from django.apps import apps

# Create your models here.

Mypointcarbon = apps.get_model('point', 'Carbonpoint')
Mypointgreen = apps.get_model('point','Greenpoint')
Myuserpoint = apps.get_model('point', 'Userpoint')
