from django.db import models

# LogIn page 
class LogIn(models.Model):
	user_name	= models.CharField(max_length=20,null=True,unique=True)
	password 	= models.CharField(max_length=20,null=True,unique=True)
