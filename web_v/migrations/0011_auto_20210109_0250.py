# Generated by Django 3.1.4 on 2021-01-08 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_v', '0010_auto_20210109_0249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lost_find_topic',
            old_name='T_F_T_date',
            new_name='L_F_T_date',
        ),
    ]
