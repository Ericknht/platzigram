"""Platzigram views."""

#Django
#para ecribir una respuesta http importamos
from django.http import HttpResponse
#para pasar un diccionario a json
from django.http import JsonResponse

# Utilities
from datetime import datetime

#siempre todas las vistas reciben un request(solicitud)
#lo que regresa es una respuesta
def hello_world(request):
	"""Return a greeting.(saludo)"""
	return HttpResponse('Oh, hi Alejandro! Current server time is {now}'.format(
		now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))

def hi(request):
	"""Hi."""
	#import pdb; pdb.set_trace()
	
	"""
	list_jason = { 'el_http': request.scheme,
					'cuerpo': request.body,
					'url_path': request.path,
					'url_path_info': request.path_info,
					'metodo': request.method,
					'cotent_type': request.content_params,
					'GET': request.GET['numbers'],
					'IP': request.META['REMOTE_ADDR'],
					'url_path_full': request.get_full_path()

	}
	return HttpResponse(list_jason.items())

	"""

	numbers = request.GET['numbers']
	print(type(numbers))
	numbers_list = numbers.split(',')

	response = JsonResponse(numbers_list, safe=False)
	return response


	
