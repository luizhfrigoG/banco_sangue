# Generated by Django 4.2.6 on 2023-10-17 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_alter_people_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='sex',
            field=models.CharField(max_length=200),
        ),
    ]