from django.shortcuts import render
from .models import SearchQuerys
from recordrecei.models import docitem_rfid
from responsible.models import respinv,rooms

def search_view(request):
	query = request.GET.get('query',None)
	user = None
	if request.user.is_authenticated:
		user = request.user
	context = {"query":query}
	if query is not None:
		SearchQuerys.objects.create(user=user,query=query)
		postrf_list = docitem_rfid.objects.search(query=query)
		context['postrf_list'] = postrf_list
		postres_list = respinv.objects.search(query=query)
		context['postres_list'] = postres_list
		postroom_list = rooms.objects.search(query=query)
		context['postroom_list'] = postroom_list
		print(query)
	return render(request,'searches/search.html',context)
