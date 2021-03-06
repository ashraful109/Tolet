# Generated by Django 4.0.1 on 2022-01-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image',
            field=models.ImageField(upload_to='house/'),
        ),
        migrations.AlterField(
            model_name='house',
            name='rent',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='slider/'),
        ),
    ]
