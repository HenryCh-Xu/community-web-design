# Generated by Django 3.1.4 on 2021-03-01 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_v', '0017_auto_20210111_2039'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entry',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
