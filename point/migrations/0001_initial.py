# Generated by Django 4.0.2 on 2022-02-14 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carbonpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pointtype', models.TextField()),
                ('cpoint', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '탄소포인트목록',
                'db_table': 'carbonlist',
            },
        ),
        migrations.CreateModel(
            name='Greenpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pointtype', models.TextField()),
                ('gpoint', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '그린포인트목록',
                'db_table': 'greenlist',
            },
        ),
        migrations.CreateModel(
            name='Userpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carbonpoint', models.IntegerField(blank=True, default=0)),
                ('greenpoint', models.IntegerField(blank=True, default=0)),
                ('carpoint', models.IntegerField(blank=True, default=0)),
                ('totalpoint', models.IntegerField(blank=True, default=0)),
                ('create_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '탄소포인트 장바구니',
            },
        ),
    ]
