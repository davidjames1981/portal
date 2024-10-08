# Generated by Django 5.1.1 on 2024-09-24 20:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contractors.contractor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Contractor',
        ),
    ]
