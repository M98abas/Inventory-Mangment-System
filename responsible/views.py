from django.contrib   						import messages
from django.shortcuts 						import render , redirect,get_object_or_404
from django.contrib.admin.views.decorators 	import staff_member_required
from .models 								import rooms,respinv
from .forms  								import Rooms,Responsible
from recordrecei.models 					import docitem_rfid
from .reander 								import RenderToPdf
from django.views.generic 					import View
from django.utils 							import timezone

@staff_member_required(login_url='Login') #made who came without of authontication go to login page
def showresp(request,id):
	try:
		qsres    = get_object_or_404(respinv,id=id)
		query1 	= qsres.resp_id.rfid_item
		print("query",query1)
		tamplate_name = 'detalersp.html'
		context = {
		"qsres":qsres,
		}
		#it's made a broch between tow pages the one in inventory and the second in responsible
		postrf_list = docitem_rfid.objects.search(query=query1)
		context['postrf_list'] = postrf_list
		return render(request, tamplate_name, context)
	except:
		template_name = 'errors/404.html'
		context = {}
		return render(request,template_name,context)

@staff_member_required(login_url='Login') #made who came without of authontication go to login page
def respon_post_create(request):
	if request.method == 'POST':
		formrom 	= Rooms(request.POST)
		formresb 	= Responsible(request.POST)
		if formrom.is_valid() and formresb.is_valid():
			obj 			 = formrom.save(commit=False)
			objresb 		 = formresb.save(commit=False)
			#bring the record that with be pK for my fk
			pe = docitem_rfid.objects.get(rfid=obj.rfid_item)
			pe.doc_items.is_stay="It's Out"
			pe.doc_items.save()
			print("Done")
			obj.rfid = pe
			obj.save()
			objresb.resp_id = obj
			objresb.save()
			messages.success(request,f"The responsible has created Successfuly ")
			return redirect('listresp')
	else:
		formrom 	= Rooms(request.POST or None)
		formresb 	= Responsible(request.POST or None)

	tamplate_name = 'AddResponsible.html'
	context = {
	'formrom' :formrom,
	'formresb':formresb,
	}
	return render(request, tamplate_name, context)

# @staff_member_required(login_url='Login') #made who came without of authontication go to login page
def res_post_list(request):
	qsro    = rooms.objects.all()
	qsres   = respinv.objects.all()
	if request.user.is_authenticated:
		my_qsro		= rooms.objects.all().values()
		my_qsres 	= respinv.objects.all().values()

		qsro  = (qsro |my_qsro).distinct()
		qsres  = (qsres |my_qsres).distinct()
	
	tamplate_name = 'respon_list.html'
	context = {
	'object_room':qsro,
	'object_resp':qsres,
	}
	return render(request, tamplate_name, context)

class PdfRnader(View):
	def get(self, request):
		qsres   = respinv.objects.all()
		today = timezone.now()
		# print(qsres.resp_id)
		params = {
		    'qsres': qsres,
			'today': today,
		    'request': request
		}
		return RenderToPdf.render('reslistpdf.html', params)


@staff_member_required(login_url='Login') #made who came without of authontication go to login page
def res_post_update(request,id):
	obj 	= get_object_or_404(rooms, id=id)
	objit 	= get_object_or_404(respinv, id=id)

	form 	= Rooms(request.POST or None,instance=obj)
	formit  = Responsible(request.POST or None,instance=objit)

	if form.is_valid() and formit.is_valid():
		form.save()
		formit.save()
		# if respinv.date_back is not None:
		# 	print("lol")
		messages.success(request,f"The responsible that has this  {obj.rfid_item} rfid is update Successfuly ")
		return redirect("listresp")
	tamplate_name = 'AddResponsible.html'
	context = {
	'formrom':form,
	'formresb':formit,
	}
	return render(request, tamplate_name, context)

@staff_member_required(login_url='Login') #made who came without of authontication go to login page
def res_post_delete(request,id):
	obj 	= get_object_or_404(rooms, id=id)
	objres 	= get_object_or_404(respinv, id=id)
	if request.method =="POST":
		obj.delete()
		objres.delete()
		pe = docitem_rfid.objects.get(rfid=obj.rfid_item)
		pe.doc_items.is_stay="It's Stay"
		pe.doc_items.save()
		messages.warning(request,f"The responsible that has this  {obj.rfid_item} rfid is deleted Successfuly ")
		return redirect("listresp")
	tamplate_name = 'deleteresp.html'
	context = {
	"object":obj,
	"objectresp":objres,
	}
	return render(request, tamplate_name, context)
