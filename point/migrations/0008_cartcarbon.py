# Generated by Django 4.0.2 on 2022-02-08 05:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('point', '0007_alter_carbonpoint_create_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartcarbon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('quantity', models.PositiveSmallIntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('carbonpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='point.carbonpoint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '탄소포인트 장바구니',
            },
        ),
    ]
