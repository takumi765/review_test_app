# Generated by Django 3.2.16 on 2022-10-22 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0004_remove_userinfo_name_test_visibility_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='percent',
            field=models.IntegerField(default=0),
        ),
    ]
