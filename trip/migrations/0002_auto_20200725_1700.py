# Generated by Django 2.2 on 2020-07-25 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='guests',
            new_name='planner',
        ),
        migrations.AddField(
            model_name='trip',
            name='plan',
            field=models.CharField(default=None, max_length=255),
        ),
    ]