# Generated by Django 4.1.7 on 2023-09-20 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('careerbot', '0004_user_delete_user_datavalues'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
