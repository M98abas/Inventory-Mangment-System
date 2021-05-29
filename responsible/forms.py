from django 			import forms
from django.forms	 	import ModelForm
from .models 			import rooms,respinv
from recordrecei.models import docitem_rfid,doc_items


class Rooms(ModelForm):

	room_id     = forms.IntegerField(label="Enter room\'s Number ",
					widget = forms.TextInput(attrs={
						'class' : 'form-control',
						'id':'room_id',
						'type':'number' ,
						'name':'room_id' ,
						'placeholder':'Room Namber'
						}))
	rfid_item   = forms.CharField(label="Enter rfid of Item ",
						widget = forms.TextInput(attrs={
							'class' : 'form-control',
							'id':'rfid_item',
							'type':'text' ,
							'name':'rfid_item' ,
							'placeholder':'rfid'
							}))

	roomName     = forms.CharField(label="Enter room\'s name ",
					widget = forms.TextInput(attrs={
						'class' : 'form-control',
						'id':'roomName',
						'type':'text' ,
						'name':'roomName' ,
						'placeholder':'Room Name'
						}))
	
	class Meta:
		model  = rooms
		fields = ('room_id','roomName','rfid_item',)

	def clean_rfid_item(self, *args, **kwargs):
		instance = self.instance
		print(instance)
		rfid = self.cleaned_data.get('rfid_item')
		qs = docitem_rfid.objects.filter(rfid__iexact=rfid) #this line of code is very helpful in the future
		print(qs)
		if instance is not None:
			qs = qs.exclude(pk=instance.pk)
		if qs.exists():
			print("done")
		else:
			raise forms.ValidationError("It's Not used ")
		return rfid

class Responsible(ModelForm):
	Name_resp 	=forms.CharField(
		label="Enter who is Responsible of this item ",
		widget=forms.TextInput(attrs={
			'class' : 'form-control',
			'id':'Name_resp',
			'type':'text' ,
			'name':'Name_resp' ,
			'placeholder':'Responsible Name'
			}))
	date_resp 	=forms.DateTimeField(
		label="Enter the date of Receipt ",
		widget=forms.DateInput(attrs={
			'class' : 'form-control',
			'id':'date_it',
			'type':'date' ,
			'name':'date' ,
			'placeholder':'Receipt date'
			}))

	date_back 	= forms.DateTimeField(
		required=False,
		label="Enter the date of back ",
		widget=forms.DateInput(attrs={
			'class' : 'form-control',
			'id':'date_it',
			'type':'date' ,
			'name':'dateBack' ,
			'placeholder':'Back date'
			}))

	class Meta:
		model  = respinv
		fields = ('Name_resp','date_resp','date_back')
