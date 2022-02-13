from django.contrib import admin
from .models import Carbonpoint, Greenpoint

# Register your models here.

class PointAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Carbonpoint, PointAdmin),
admin.site.register(Greenpoint, PointAdmin),