# Generated by Django 2.1.5 on 2019-01-18 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0003_auto_20190117_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='name',
            new_name='nombre',
        ),
    ]
