from django.db import models

class UserDatabase(models.Model):

    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    date = models.DateField()

    def __str__(self):
        return self.name