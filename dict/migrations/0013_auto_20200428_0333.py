# Generated by Django 2.2.7 on 2020-04-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0012_auto_20200428_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='word',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
