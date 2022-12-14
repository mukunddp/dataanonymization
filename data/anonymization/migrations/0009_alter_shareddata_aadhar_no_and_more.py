# Generated by Django 4.0.4 on 2022-05-06 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonymization', '0008_alter_shareddata_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareddata',
            name='aadhar_no',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='shareddata',
            name='account_no',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='shareddata',
            name='account_type',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='shareddata',
            name='age',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='shareddata',
            name='dob',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='shareddata',
            name='fathers_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='shareddata',
            name='first_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='shareddata',
            name='last_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='shareddata',
            name='mail_id',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='shareddata',
            name='mobile_no',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='shareddata',
            name='occupation',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='shareddata',
            name='pan_no',
            field=models.CharField(max_length=500),
        ),
    ]
