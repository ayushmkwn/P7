# Generated by Django 3.2.8 on 2021-10-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_userprofile_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile',
            field=models.ImageField(default=0, upload_to='images/'),
            preserve_default=False,
        ),
    ]
