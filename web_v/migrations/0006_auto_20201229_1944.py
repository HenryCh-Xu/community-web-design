# Generated by Django 3.1.4 on 2020-12-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_v', '0005_auto_20201229_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lost_find_topic',
            name='dete',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
