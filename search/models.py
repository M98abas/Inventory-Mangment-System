from django.conf import settings
from django.db import models

# Create your models here.

class SearchQuerys(models.Model):
	user 	= models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True, on_delete=models.SET_NULL)
	query 	= models.CharField(max_length=120)
	timestamp = models.DateTimeField(auto_now_add=True)
