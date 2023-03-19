from django.db import migrations
from csv import DictReader
from main.models import Restaurant


def seed_database(apps, schema_editor):
    for row in DictReader(open('restaurantes.csv', encoding="utf8")):
        restaurant = Restaurant(
            id = row['id'],
            rating = row['rating'],
            name = row['name'],
            site = row['site'],
            email = row['email'],
            phone = row['phone'],
            street = row['street'],
            city = row['city'],
            state = row['state'],
            lat = row['lat'],
            lng = row['lng']
        )
        restaurant.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_database)
    ]
