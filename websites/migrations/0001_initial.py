# Generated by Django 4.1.5 on 2023-01-22 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=64)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]
