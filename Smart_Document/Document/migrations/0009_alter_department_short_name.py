# Generated by Django 5.1.2 on 2025-05-20 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Document', '0008_department_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='short_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
