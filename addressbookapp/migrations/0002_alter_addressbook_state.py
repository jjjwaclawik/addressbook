# Generated by Django 5.0.7 on 2024-07-29 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addressbookapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressbook',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressbookapp.state'),
        ),
    ]
