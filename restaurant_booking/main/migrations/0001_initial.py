# Generated by Django 4.1.7 on 2023-03-18 22:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('name', models.TextField()),
                ('site', models.TextField(validators=[django.core.validators.URLValidator])),
                ('email', models.TextField(validators=[django.core.validators.EmailValidator()])),
                ('phone', models.TextField()),
                ('street', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
    ]