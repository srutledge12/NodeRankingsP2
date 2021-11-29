# Generated by Django 3.2.5 on 2021-11-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0003_delete_user'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='packagedata',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('Content__isnull', False), ('URL__isnull', True)), models.Q(('Content__isnull', True), ('URL__isnull', False)), _connector='OR'), name='only_one_content_type'),
        ),
    ]
