# Generated by Django 3.2.5 on 2021-11-11 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0020_auto_20211111_1245'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='packagedata',
            name='registry_packagedata_content_or_url',
        ),
    ]
