# Generated by Django 2.2.7 on 2019-11-26 07:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('esearch', models.TextField()),
                ('eentry', models.TextField()),
                ('tentry', models.TextField()),
                ('ecat', models.TextField()),
                ('ethai', models.TextField()),
                ('esyn', models.TextField()),
                ('eant', models.TextField()),
            ],
        ),
    ]
