# Generated by Django 2.1 on 2019-10-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_auto_20191004_2235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='candidate',
            new_name='candidate_id',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='poll',
            new_name='poll_id',
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=1),
        ),
    ]