# virtualenv (employee_managementemployee_management_latest)

from django.db import models

# Create your models here.
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Employee(models.Model):
    EMPLOYEE_TYPE_CHOICES = [
        ('1099', '1099'),
        ('W2', 'W2'),
    ]

    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='employees', null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    dob = models.DateField()  # Date of Birth
    department = models.CharField(max_length=100)
    emergency_contact = models.CharField(max_length=15)
    home_address = models.TextField()
    work_address = models.TextField()
    employee_type = models.CharField(
        max_length=4,
        choices=EMPLOYEE_TYPE_CHOICES,
        default='W2'
    )
    travel_document = models.ImageField(upload_to='documents/', null=True, blank=True)  # Upload for file/image
    social_security = models.CharField(max_length=9, null=True, blank=True)

    def __str__(self):
        return self.name
