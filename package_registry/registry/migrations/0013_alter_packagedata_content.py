# Generated by Django 3.2.5 on 2021-11-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0012_alter_packagedata_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagedata',
            name='Content',
            field=models.TextField(blank=True),
        ),
    ]