# Generated by Django 2.0.4 on 2018-04-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_type', '0006_auto_20180404_0109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musicsubtype',
            name='music_type',
        ),
        migrations.AddField(
            model_name='musictype',
            name='music_sub_type',
            field=models.ManyToManyField(to='music_type.MusicSubType'),
        ),
    ]
