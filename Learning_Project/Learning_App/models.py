from django.db import models

# Create your models here.
class Information(models.Model):
    Name = models.CharField(max_length=100)
    ID = models.AutoField(primary_key=True)
    Contact = models.IntegerField()
    Address = models.CharField(max_length=300)
