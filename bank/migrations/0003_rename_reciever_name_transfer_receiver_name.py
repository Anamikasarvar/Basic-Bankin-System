# Generated by Django 3.2.4 on 2021-07-13 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_transfer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transfer',
            old_name='reciever_name',
            new_name='receiver_name',
        ),
    ]
