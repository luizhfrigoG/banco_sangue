# Generated by Django 4.2.6 on 2023-10-17 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('type', '0001_initial'),
        ('people', '0005_alter_people_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='type_blood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type_blood', to='type.type'),
        ),
    ]
