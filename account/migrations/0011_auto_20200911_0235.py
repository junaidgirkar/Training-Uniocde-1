# Generated by Django 3.1 on 2020-09-10 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200911_0231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='course',
            new_name='subject',
        ),
    ]
