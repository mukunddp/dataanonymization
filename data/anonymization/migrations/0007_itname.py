# Generated by Django 4.0.4 on 2022-05-05 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonymization', '0006_banknames'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
    ]