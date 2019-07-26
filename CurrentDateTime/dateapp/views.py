from django.shortcuts import render
from django.http.response import HttpResponse
import datetime as dt

date = dt.datetime.now()

def dateviews(request):
	return HttpResponse("<h1> The Current date and Time is {}</h1>".format(date))


# Create your views here.
