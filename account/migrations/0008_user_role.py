# Generated by Django 3.1 on 2020-09-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20200909_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='Default', max_length=255),
            preserve_default=False,
        ),
    ]
