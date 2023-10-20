from django.db import models

class Type(models.Model):
    blood = models.CharField(max_length=3)


    def __str__(self):
        return self.blood
