# Generated by Django 4.0.4 on 2022-05-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonymization', '0005_alter_shareddata_it_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='bankNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
    ]
