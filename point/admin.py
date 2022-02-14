from django.contrib import admin
from .models import Carbonpoint, Greenpoint,Carpoint, Userpoint


# Register your models here.

class PointAdmin(admin.ModelAdmin):
    search_fields = ['id', 'subject', 'username']

admin.site.register(Carbonpoint, PointAdmin),
admin.site.register(Greenpoint, PointAdmin),
admin.site.register(Carpoint, PointAdmin),
admin.site.register(Userpoint, PointAdmin),
