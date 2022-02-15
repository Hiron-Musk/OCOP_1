from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Carbonpoint(models.Model):
    pointtype = models.TextField()
    cpoint = models.IntegerField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'carbonlist'
        verbose_name = '탄소포인트목록'
    def __str__(self):
        return self.pointtype

class Greenpoint(models.Model):
    pointtype = models.TextField()
    gpoint = models.IntegerField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'greenlist'
        verbose_name = '그린포인트목록'
    def __str__(self):
        return self.pointtype

class Carpoint(models.Model):
    carpoint=models.IntegerField()

    class Meta:
        db_table = 'Carpoint'
        verbose_name = '자동차탄소포인트'



class Userpoint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carbonpoint = models.IntegerField(blank=True, default=0)
    greenpoint = models.IntegerField(blank=True, default=0)
    vehiclepoint = models.IntegerField(blank=True, default=0)
    totalpoint = models.IntegerField(blank=True, default=0)
    create_date = models.DateTimeField(editable=True)

    class Meta:
        verbose_name = '탄소포인트 장바구니'

    def sub_total(self):
        return self.carbonpoint

    def __str__(self):
        return self.user.username

