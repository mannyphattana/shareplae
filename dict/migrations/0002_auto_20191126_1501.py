# Generated by Django 2.2.7 on 2019-11-26 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]