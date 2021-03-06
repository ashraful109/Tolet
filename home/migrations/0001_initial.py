# Generated by Django 4.0.1 on 2022-01-28 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('rent', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='house')),
                ('location', models.CharField(max_length=200)),
                ('house_type', models.CharField(max_length=250)),
                ('area', models.CharField(max_length=50)),
                ('beds', models.CharField(max_length=20)),
                ('baths', models.CharField(max_length=20)),
                ('garage', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slider')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.house')),
            ],
        ),
    ]
