# Generated by Django 4.1.5 on 2023-01-24 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('websites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('added_on', models.DateTimeField(auto_now=True)),
                ('last_modified', models.DateTimeField(blank=True, default=None, null=True)),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_credentials', to='websites.website')),
            ],
        ),
    ]