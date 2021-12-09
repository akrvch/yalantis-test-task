from django.db import models


class Driver(models.Model):
    """Driver model."""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Vehicle(models.Model):
    """Vehicle model."""
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    plate_number = models.CharField(max_length=8, help_text="Use the following format: 'AA1111BP'", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
