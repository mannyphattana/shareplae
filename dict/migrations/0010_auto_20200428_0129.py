# Generated by Django 2.2.7 on 2020-04-27 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0009_auto_20200428_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
