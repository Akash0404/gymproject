from django.db import models

# Create your models here.
class registerr(models.Model):
    Username = models.CharField(max_length=50)
    Password =models.CharField(max_length=50)
    Firstname =models.CharField(max_length=50)
    Lastname =models.CharField(max_length=50)
    # def __str__(self):
    #     return self.name

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    Contact_no = models.CharField(max_length=10)
    subject = models.CharField(max_length=40)
    messages = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
   

class Enquiry(models.Model):
    name = models.CharField(max_length=60)
    contact = models.CharField(max_length=10)
    emailid = models.CharField(max_length=60)
    age = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    unit = models.CharField(max_length=10)
    date = models.CharField(max_length=40)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
class Plan(models.Model):
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=10)
    duration = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    emailid = models.CharField(max_length=50)
    age = models.CharField(max_length=40)
    gender = models.CharField(max_length=10, default="")
    plan = models.CharField(max_length=50)
    joindate = models.DateField(max_length=40)
    expiredate = models.DateField(max_length=40)
    initialamount = models.CharField(max_length=10)


    def __str__(self):
        return self.name