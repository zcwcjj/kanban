from django.db import models

# Create your models here.
class Pic(models.Model):
	photo = models.ImageField(upload_to='cars')


