# Generated by Django 4.1.7 on 2023-04-15 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_password_signup_password1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
