# Generated by Django 3.1.4 on 2021-01-11 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_v', '0016_electronics_entry_electronics_topic_necessary_entry_necessary_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='electronics_entry',
            options={'verbose_name_plural': 'Electronics_topic_entries'},
        ),
        migrations.AlterModelOptions(
            name='lost_find_entry',
            options={'verbose_name_plural': 'Lost_find_topic_entries'},
        ),
        migrations.AlterModelOptions(
            name='necessary_entry',
            options={'verbose_name_plural': 'Necessary_topic_entries'},
        ),
    ]
