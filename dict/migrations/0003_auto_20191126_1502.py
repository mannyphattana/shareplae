# Generated by Django 2.2.7 on 2019-11-26 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0002_auto_20191126_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='eant',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='esyn',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='ethai',
            field=models.TextField(null=True),
        ),
    ]