# Generated by Django 4.1.5 on 2023-01-21 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0002_alter_website_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='password',
            old_name='add_on',
            new_name='added_on',
        ),
    ]