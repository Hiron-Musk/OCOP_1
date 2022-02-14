import django
django.setup()

from django.db import models
from django.apps import apps
# from point.models import Carbonpoint

# Create your models here.

Mypointcarbon = apps.get_model('point', 'Carbonpoint')
Mypointgreen = apps.get_model('point','Greenpoint')
# Userpoint = apps.get_model('point', 'Userpoint')
