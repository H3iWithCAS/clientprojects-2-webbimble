from django.db import models

class Child(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    parent_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name