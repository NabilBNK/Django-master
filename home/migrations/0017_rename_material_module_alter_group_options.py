# Generated by Django 4.1.7 on 2023-05-11 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_remove_teacherextra_group_teacherextra_groups'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='material',
            new_name='module',
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['name']},
        ),
    ]