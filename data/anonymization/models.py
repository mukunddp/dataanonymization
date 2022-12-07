from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    department = models.CharField(max_length=20)


class bankUser(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    fathers_name = models.CharField(max_length=200)
    age = models.IntegerField()
    dob = models.DateField()
    mobile_no = models.BigIntegerField()
    mail_id = models.EmailField()
    address = models.CharField(max_length=500)
    occupation = models.CharField(max_length=100)

    account_no = models.BigIntegerField()
    account_type = models.CharField(max_length=50)
    pan_no = models.CharField(max_length=50)
    aadhar_no = models.BigIntegerField()
    balance = models.BigIntegerField()


class bankProfile(models.Model):
    user = models.ForeignKey('anonymization.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mobile_no = models.BigIntegerField()
    mail_id = models.EmailField()
    address = models.CharField(max_length=500)
    organization = models.CharField(max_length=200)


class itProfile(models.Model):
    user = models.ForeignKey('anonymization.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mobile_no = models.BigIntegerField()
    mail_id = models.EmailField()
    address = models.CharField(max_length=500)
    organization = models.CharField(max_length=200)


class sharedData(models.Model):
    it_man = models.ForeignKey('anonymization.itProfile', on_delete=models.CASCADE)
    it_user_id = models.ForeignKey('anonymization.User', on_delete=models.CASCADE)
    bank_man = models.ForeignKey('anonymization.bankProfile', on_delete=models.CASCADE)
    bank_man_user = models.IntegerField()
    name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)

    bank_user = models.ForeignKey('anonymization.bankUser', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    fathers_name = models.CharField(max_length=500)
    age = models.CharField(max_length=500)
    dob = models.CharField(max_length=500)
    mobile_no = models.CharField(max_length=500)
    mail_id = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    occupation = models.CharField(max_length=500)
    account_no = models.CharField(max_length=500)
    account_type = models.CharField(max_length=500)
    pan_no = models.CharField(max_length=500)
    aadhar_no = models.CharField(max_length=500)
    balance = models.CharField(max_length=500)


class bankNames(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)


class ItName(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)