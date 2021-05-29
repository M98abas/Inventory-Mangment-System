from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import Loginform,loginmodel

# @staff_member_required


def index(request):
    return render(request,'index.html')

@staff_member_required(login_url='Login')
def special(request):
    return HttpResponseRedirect(reverse('index'))

# @staff_member_required(login_url='Login')
def user_logout(request):
	if request.method == 'POST':
		logout(request)
		return redirect('Indexing')



def user_login(request):
	try:
		form = AuthenticationForm(data=request.POST or None)
		if request.method == 'POST':
			form = AuthenticationForm(data=request.POST or None)
			if form.is_valid():
				user_name=form.get_user()
				login(request,user_name)
				return redirect('Indexing')
			else:
				raise Http404()
		context =  {
		'form':form
		}
		return render(request, 'login.html',context)
	except:
		context = {}
		template_name = 'errors/401.html'
		return render(request,template_name,context)



def server_error(request):
    return render(request, 'errors/500.html')
def not_found(request,exception):
	return render(request,'errors/404.html', status=404)
def permission_denied(request):
    return render(request, 'errors/401.html')