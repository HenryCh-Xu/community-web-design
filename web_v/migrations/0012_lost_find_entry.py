# Generated by Django 3.1.4 on 2021-01-08 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_v', '0011_auto_20210109_0250'),
    ]

    operations = [
        migrations.CreateModel(
            name='lost_find_entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('L_F_T_date', models.DateTimeField(auto_now_add=True)),
                ('L_F_T', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_v.lost_find_topic')),
            ],
        ),
    ]
