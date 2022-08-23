from django.db import models

class Contact (models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=False, null=False)
    company = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.name 

