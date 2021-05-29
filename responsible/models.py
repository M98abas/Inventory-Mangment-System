from django.db import models
from recordrecei.models import docitem_rfid

class PostroomQuerySet(models.QuerySet):
	def search(self,query):
		return self.filter(rfid_item__iexact=query)


class PostroomManager(models.Manager):
	def get_queryset(self):
		return PostroomQuerySet(self.model,using=self._db)

	def search(self,query=None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().search(query)






class rooms(models.Model):
	room_id 	= models.IntegerField(null=True,blank=True)
	rfid_item 	= models.CharField(max_length=40,null=True,blank=True)
	roomName 	= models.CharField(max_length=120)
	rfid 		= models.ForeignKey(docitem_rfid,null=True,on_delete=models.SET_NULL)
	objects 	= PostroomManager()
	def __str__(self):
		return str(self.room_id)


class PostrespQuerySet(models.QuerySet):
	def search(self,query):
		return self.filter(Name_resp__iexact=query)


class PostrespManager(models.Manager):
	def get_queryset(self):
		return PostrespQuerySet(self.model,using=self._db)

	def search(self,query=None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().search(query)


class respinv(models.Model):
	Name_resp 	= models.CharField(max_length=120)
	date_resp 	= models.DateField(null=True,blank=True)
	date_back 	= models.DateField(null=True)
	resp_id 	= models.ForeignKey(rooms,null=True,blank=True,on_delete=models.CASCADE)
	objects 	= PostrespManager()


	def __int__(self):
		return int(self.id)

# class OldUser(models.Model):
# 	rfid 	 = models.CharField(max_length=120)