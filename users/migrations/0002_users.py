# Generated by Django 3.1.7 on 2021-03-24 15:08

from django.db import migrations

def create_data(apps, schema_editor):
    User = apps.get_model('users', 'User')
    User(name = "User 001", email="user001@email.com", phone="00000000", address="User 000 Address", description="User 001 description").save()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]