# Generated by Django 4.0.5 on 2022-06-12 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvbuilder', '0002_rename_company_id_experience_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='start_date',
        ),
    ]
