from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

def sessionview(request):
    return HttpResponse("Hello, world. 6da987f4 is the seesionview.")


