from django.db import models

# Create your models here.

class coinbase(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email
