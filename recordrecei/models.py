from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import Q




class items(models.Model):
	name 		= models.CharField(max_length=120)
	item_number	= models.IntegerField(null=True,blank=True)



class documents(models.Model):
	date_it 	= models.DateField(null=True,blank=True)



# detial of document items work
class doc_items(models.Model):
	id_items    = models.ForeignKey(items,on_delete=models.CASCADE)
	ID_doc 	    = models.ForeignKey(documents,on_delete=models.CASCADE)
	quantity 	= models.IntegerField(null=True,blank=True)
	source 		= models.CharField(max_length=300)
	price 		= models.FloatField()
	is_stay 	= models.CharField(max_length=20,default="It's Stay")


User = settings.AUTH_USER_MODEL

class PostItemQuerySet(models.QuerySet):
	def search(self,query):
		return self.filter(rfid__iexact=query)


class PostItemsManager(models.Manager):
	def get_queryset(self):
		return PostItemQuerySet(self.model,using=self._db)

	def search(self,query=None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().search(query)




# every work of record Reiciving Table 
class docitem_rfid(models.Model):
	rfid 		= models.CharField(max_length=50,null=True,unique=True)
	doc_items 	= models.ForeignKey(doc_items,on_delete=models.CASCADE)
	objects 	= PostItemsManager() 
	
	def __str__(self):
		return str(self.rfid)