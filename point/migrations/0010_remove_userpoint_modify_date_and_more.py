# Generated by Django 4.0.2 on 2022-02-13 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point', '0009_userpoint_remove_cartcarbon_carbonpoint_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpoint',
            name='modify_date',
        ),
        migrations.AlterField(
            model_name='userpoint',
            name='create_date',
            field=models.DateTimeField(),
        ),
    ]
