# Generated by Django 2.2 on 2019-06-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20190403_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='f_name',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_details',
            name='l_name',
            field=models.CharField(default='not a/v', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_details',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
