# Generated by Django 2.2 on 2022-06-03 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsz_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='outtable',
            name='military_rank',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
