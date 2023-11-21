from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    business_email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.business_email