# Generated by Django 2.2.7 on 2020-04-26 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0006_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        )
    ]