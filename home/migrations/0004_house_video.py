# Generated by Django 4.0.1 on 2022-02-11 19:26

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_house_options_house_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]