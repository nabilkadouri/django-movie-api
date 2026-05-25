from django.db import models

class Director(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} "