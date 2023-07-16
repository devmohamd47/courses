from typing import Any, Iterable, Optional
from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

# Create your models here.

class Course(models.Model):
    CHOICES =(
    ("1", "حضوري"),
    ("2", "الكتروني"),
)
    
    CHOICES2 =(
    ("M", "ذكر"),
    ("F", "انثى"),
)
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.IntegerField(validators=[MaxValueValidator(9999)])
    description = models.CharField(max_length=100)
    longdescription = models.CharField(max_length=5000, null=True)
    trainer = models.CharField(max_length=20)
    trainerDescription = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    type = models.CharField(max_length=1, choices= CHOICES)
    trainerGender = models.CharField(max_length=1, choices= CHOICES2)
    discount = models.IntegerField(validators=[MaxValueValidator(100)])
    selected = models.BooleanField(default=False)

    
class TeachRequest(models.Model):
    name = models.CharField(max_length=20)
    phone_regex = RegexValidator(
        regex=r'^\+?\d{9,15}$',  # Customize the regex pattern as per your phone number format
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = models.CharField(max_length=15, validators=[phone_regex])
    description = models.CharField(max_length=1000)

class Post(models.Model):
    title = models.CharField(max_length=20)
    shortDescription = models.CharField(max_length=200)
    longDescription = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
 
    
class MsgRequest(models.Model):
    name = models.CharField(max_length=20)
    phone_regex = RegexValidator(
        regex=r'^\+?\d{9,15}$',  # Customize the regex pattern as per your phone number format
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = models.CharField(max_length=15, validators=[phone_regex])
    msg = models.CharField(max_length=2000)