# Generated by Django 4.2 on 2024-08-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentistry', '0003_alter_doctors_specialization_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='description_doctor',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
