# Generated by Django 2.2.7 on 2019-11-26 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0003_auto_20191126_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
