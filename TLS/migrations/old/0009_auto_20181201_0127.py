# Generated by Django 2.1.1 on 2018-12-01 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TLS', '0008_submissionsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissionsmodel',
            name='filenames',
            field=models.CharField(default=1, max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submissionsmodel',
            name='numberOfFiles',
            field=models.CharField(default=1, max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submissionsmodel',
            name='uploadPath',
            field=models.CharField(default=1, max_length=512),
            preserve_default=False,
        ),
    ]
