from django import forms
from django.forms import ModelForm
from .models import docitem_rfid,doc_items,items,documents


class docitrfidmodel(ModelForm):
	rfid     = forms.CharField(label="Enter RfID ",widget=forms.TextInput(attrs={'class' : 'form-control','id':'rfid','type':'text' ,'name':'rfid' ,'placeholder':'rfid'}))

	class Meta:
		model  = docitem_rfid
		fields = ('rfid',)

	def clean_rfid(self, *args, **kwargs):
		instance = self.instance
		print(instance)
		rfid = self.cleaned_data.get('rfid')
		qs = docitem_rfid.objects.filter(rfid__iexact=rfid) #this line of code is very helpful in the future
		if instance is not None:
			qs = qs.exclude(pk=instance.pk)
		if qs.exists():
			raise forms.ValidationError("It's used")
		return rfid

class itemdetale(ModelForm):
	item_number  = forms.CharField(label="Enter Number item in your file ",widget=forms.TextInput(attrs={'class' : 'form-control','id':'item_number','type':'number' ,'name':'number' ,'placeholder':'Item\'s Number'}))
	name 		 = forms.CharField(label="Name of Item's ",widget=forms.Textarea(attrs={'class' : 'form-control','id':'name_item','type':'text' ,'name':'NameItem' ,'placeholder':'Name of Item'}))
	class Meta:
		model 	 = items
		fields   = ('item_number','name')

class quntitsource(ModelForm):
	source  	 = forms.CharField(label="The source of item ",widget=forms.Textarea(attrs={'class' : 'form-control','id':'source','type':'text' ,'name':'source' ,'placeholder':'Item Source'}))
	quantity 	 = forms.IntegerField(label="Quantity of item ",widget=forms.TextInput(attrs={'class' : 'form-control','id':'quantity','type':'number' ,'name':'Quantity' ,'placeholder':'Quantity'}))
	price 	 	 = forms.FloatField(label="Price of item ",widget=forms.TextInput(attrs={'class' : 'form-control','id':'price','type':'numbers' ,'name':'price' ,'placeholder':'Price in IQD'}))

	class Meta:
		model 	 = doc_items
		fields 	 = ('source','quantity','price')

class documentsFi(ModelForm):
	date_it  	 = forms.DateTimeField(label="Enter the date ",widget=forms.DateInput(attrs={'class' : 'form-control','id':'date_it','type':'date' ,'name':'date' ,'placeholder':'Date Puying'}))

	class Meta:																	
		model 	 = documents
		fields 	 = ('date_it',)
