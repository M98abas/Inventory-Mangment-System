"""Infenmangmentsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib     import admin
from django.urls        import path,include
from login.views        import index,user_login,user_logout,server_error,not_found,permission_denied
from search.views       import search_view 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',index,name='Indexing'),
    path('Login/',user_login,name='Login'),
    path('user_logout/',user_logout,name='logout'),
    path('',include('recordrecei.urls')),
    path('',include('responsible.urls')),
    path('search/',search_view,name='searchrfid'),
]