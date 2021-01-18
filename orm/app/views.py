from django.shortcuts import render,HttpResponse,redirect

def students(request):
    if request.method == "POST": 
        return HttpResponse("aca los students Metodo POST")
    else:
        return HttpResponse("Aca ingreso metodo GET")

