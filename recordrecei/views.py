from django.http 							import HttpResponseRedirect
from django.urls 							import reverse
from .render 								import RenderToPdf
from django.views.generic 					import View
from django.shortcuts 						import render , redirect,get_object_or_404
from .forms 								import docitrfidmodel,itemdetale,quntitsource,documentsFi
from django.contrib.admin.views.decorators 	import staff_member_required
from .models 								import docitem_rfid,doc_items,items,documents
from responsible.models 					import respinv,rooms
from django.contrib 						import messages
from django.utils 							import timezone


def showitem(request,id):
	try:
		qsrf 	  = get_object_or_404(docitem_rfid,id=id)
		qsqun     = get_object_or_404(doc_items,id=id)
		query1 	  = qsrf.rfid
		print("query",query1)
		# print(doc_items.objects.all())
		tamplate_name = 'detalitem.html'
		context = {
		"qsrf":qsrf,
		"qsqun":qsqun,
		}

		postrf_list = rooms.objects.search(query=query1)
		context['postrf_list'] = postrf_list
		return render(request, tamplate_name, context)
	except:
		tamplate_name = 'errors/404.html'
		context = {}
		return render(request, tamplate_name, context)



@staff_member_required(login_url='Login') #made who came without of authontication go to login page
def item_post_create(request):

	if request.method == 'POST':
		form 	= docitrfidmodel(request.POST)
		formit  = itemdetale(request.POST)
		formqun = quntitsource(request.POST)
		formda  = documentsFi(request.POST)	
		if form.is_valid() and formit.is_valid() and formqun.is_valid() and formda.is_valid():
			obj 	= form.save(commit=False)
			objit 	= formit.save(commit=False)
			objdet  = formqun.save(commit=False)
			objda 	= formda.save(commit=False)
			objdet.id_items = objit
			objdet.ID_doc = objda
			objda.save()
			objit.save()
			objdet.save()
			obj.doc_items=objdet
			obj.save()
			objda.save()
			messages.success(request,f"The item has created Successfuly ")
			return redirect('report')
	else:

		form 	= docitrfidmodel(request.POST or None)
		formit  = itemdetale(request.POST or None)
		formqun = quntitsource(request.POST or None)
		formda  = documentsFi(request.POST or None)	


	tamplate_name = 'create.html'
	context = {
	'form' :form,
	'formit':formit,
	'formqun':formqun,
	'formdate':formda
	}
	return render(request, tamplate_name, context)

def item_post_list(request):
	qsrf 	= docitem_rfid.objects.all()

	if request.user.is_authenticated:
		my_qs 		= docitem_rfid.objects.filter(id=1)
		qsrf  = (qsrf |my_qs).distinct()
	tamplate_name = 'reports.html'
	context = {

	'object_listrf':qsrf,
	}
	return render(request, tamplate_name, context)

class PdfRnader(View):
    def get(self, request):
        qsrf 	= docitem_rfid.objects.all()
        today = timezone.now()
        print(request.user)
        params = {
            'qsrf': qsrf,
			'today': today,
            'request': request
        }
        return RenderToPdf.render('listpdf.html', params)


@staff_member_required(login_url='Login') #made who came without of authontication go to login page
def item_post_update(request,id):
	obj 	= get_object_or_404(docitem_rfid, id=id)
	objit 	= get_object_or_404(items, id=id)
	objdoc 	= get_object_or_404(doc_items, id=id)
	objda 	= get_object_or_404(documents,id=id)

	form 	= docitrfidmodel(request.POST or None,instance=obj)
	formit  = itemdetale(request.POST or None,instance=objit)
	formqun = quntitsource(request.POST or None,instance=objdoc)
	formda  = documentsFi(request.POST  or None,instance=objda)	

	if form.is_valid() and formit.is_valid() and formqun.is_valid() and formda.is_valid():
		form.save()
		formit.save()
		formqun.save()
		formda.save()
		messages.success(request,f"The Item that has this  {obj.rfid} rfid is update Successfuly ")

		return redirect("report")
	tamplate_name = 'create.html'
	context = {
	'form':form,
	'formit':formit,
	'formqun':formqun,
	'formdate':formda
	}
	return render(request, tamplate_name, context)
@staff_member_required(login_url='Login') #made who came without of authontication go to login page
def item_post_delete(request,id):
	obj 	= get_object_or_404(docitem_rfid, id=id)
	objit 	= get_object_or_404(items, id=id)
	objdoc 	= get_object_or_404(doc_items, id=id)
	objda 	= get_object_or_404(documents,id=id)

	if request.method =="POST":
		obj.delete()
		objit.delete()
		objdoc.delete()
		objda.delete()
		messages.warning(request,f"The Item that has this  {obj.rfid} rfid is deleted Successfuly ")

		return redirect("report")
	tamplate_name = 'delete.html'
	context = {
	"object":obj,
	"objectit":objit,
	"objectdoc":objdoc,
	"objectdate":objda
	}
	return render(request, tamplate_name, context)


