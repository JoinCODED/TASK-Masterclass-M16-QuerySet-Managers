# Generated by Django 4.0.5 on 2022-06-29 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0002_genre_created_at_genre_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]