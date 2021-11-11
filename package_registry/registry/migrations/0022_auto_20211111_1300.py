# Generated by Django 3.2.5 on 2021-11-11 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0021_remove_packagedata_registry_packagedata_content_or_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagedata',
            name='Content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='packagedata',
            name='URL',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
