# Generated by Django 5.1.1 on 2024-09-23 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contractor',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
