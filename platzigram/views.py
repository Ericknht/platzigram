"""Platzigram views."""

#Django
#para ecribir una respuesta http importamos
from django.http import HttpResponse
#para pasar un diccionario a json
from django.http import JsonResponse

# Utilities
from datetime import datetime
import json

#siempre todas las vistas reciben un request(solicitud)
#lo que regresa es una respuesta
def hello_world(request):
	"""Return a greeting.(saludo)"""
	return HttpResponse('Oh, hi Alejandro! Current server time is {now}'.format(
		now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))

def json_sorted_ints(request):
	"""Return a JSON response with sorted integers"""
	

	numbers = [int(i) for i in request.GET['numbers'].split(',')]
	sorted_ints = sorted(numbers)
	#import pdb; pdb.set_trace()
	data = {
		'status': 'ok',
		'numbers': sorted_ints,
		'message': 'Integers sorted successfully'
	}

	return HttpResponse(
		json.dumps(data,indent=4), 
		content_type="application/json"
	)

	#return JsonResponse(sorted_ints, safe=False)
	#return JsonResponse(data, json_dumps_params = {'indent': 4})

def hi(request, name, age):

	if age > 18:
		message = 'Hi {} your age is: {}, you are adult'.format(name,age)
	else:
		message ='Hi {} your age is: {}, you are a child'.format(name,age)

	return HttpResponse(message)