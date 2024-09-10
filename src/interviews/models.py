from django.db import models

# Create your models here.

class Interview(models.Model):
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    description = models.TextField()
    skills = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.company} - {self.date}"
