# Generated by Django 5.1.4 on 2024-12-17 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0004_alter_tbl_userprofile_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_userprofile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
