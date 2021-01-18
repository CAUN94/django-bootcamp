from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
def another(request,myval):
	msg = f'Today is {myval}'
	return HttpResponse(msg)

def plantilla(request):
	return render(request, "index.html")


def name(request):
	data = {
		'name': 'Cris',
		'last_name': 'Ugarte'
	}
	return render(request, 'contact.html',data)
