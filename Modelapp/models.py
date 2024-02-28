from django.db import models


class students(models.Model):
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    Email_address = models.CharField(max_length=20)
    DOB = models.DateField()
    Age = models.IntegerField()

    class Meta:
        db_table = "wanafunzi"


class Teachers(models.Model):
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    Email_address = models.CharField(max_length=20)

    def __str__(self):
        return self.Firstname


class Parents(models.Model):
    Fullnames = models.CharField(max_length=20)
    Email_address = models.CharField(max_length=20)
    DOB = models.DateField()
    Age = models.IntegerField()

    def __str__(self):
        return self.Fullnames


class Post(models.Model):
    Title = models.CharField(max_length=20)
    Description = models.CharField(max_length=20)
    Author = models.CharField(max_length=20)
    Created_at = models.DateTimeField()

    def __str__(self):
        return self.Title


