# Generated by Django 3.2.4 on 2021-07-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=400)),
                ('amount', models.IntegerField()),
                ('reciever_name', models.CharField(max_length=50)),
            ],
        ),
    ]
