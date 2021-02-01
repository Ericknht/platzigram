"""Platzigram URLs module."""

"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from platzigram import views as local_views
#from posts import views as posts_views
#from users import views as users_views

urlpatterns = [
	#path defines cual es la url que estás esperando responder algo
	#1er argumento es la url
	#el algo que tiene que pasar es el 2do argumento, es la vista, una vista en django es simplemente una función o una clase
    path('admin/', admin.site.urls),

    #path('hello-world',local_views.hello_world, name='hello_world'),
    #path('hi/<str:name>/<int:age>/',local_views.hi, name='hi'),
    #path('sorted/',local_views.json_sorted_ints, name='sort'),


    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users'))

    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
