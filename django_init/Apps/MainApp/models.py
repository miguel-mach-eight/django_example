from django.db import models

# Create your models here.
class Person(models.Model):
	id = models.AutoField(primary_key = True)
	FirstName = models.CharField(max_length = 100)
	LastName = models.charField(max_length = 120)
	email = models.EmailField(max_length = 200)