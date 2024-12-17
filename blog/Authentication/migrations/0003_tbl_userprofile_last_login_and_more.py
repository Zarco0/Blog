# Generated by Django 5.1.4 on 2024-12-17 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0002_tbl_logintable'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_userprofile',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tbl_userprofile',
            name='reset_code',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]