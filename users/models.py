from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import admin
from django.core.validators import MinValueValidator

class CustomUser(AbstractUser):
    # add additional fields in here
    uploads = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    
    def __str__(self):
	"""!@ Returns user's email. 
	"""
        return self.email

    def __unicode__(self):
	"""!@ Returns user's ID. 
	"""
        return self.uploads  


    def incUploads(self):
	"""!@ Returns user's upload +1 to increment it. 
	"""
        self.uploads += 1

    def getUploads(self):
	"""!@ Returns user's upload. 
	"""
        return self.uploads

    

