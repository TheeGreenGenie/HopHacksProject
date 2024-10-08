# Generated by Django 5.1 on 2024-09-15 06:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=25)),
                ('age', models.CharField(max_length=5)),
                ('risk', models.CharField(max_length=25)),
                ('income', models.CharField(max_length=25)),
                ('disposable_income', models.CharField(max_length=25)),
                ('goal1', models.CharField(max_length=60)),
                ('goal2', models.CharField(max_length=60)),
                ('goal3', models.CharField(max_length=60)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
