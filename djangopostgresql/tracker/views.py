from django.shortcuts import render
from django.http import HttpResponse
from .models import Tracker

# Create your views here.
def index(request):
	test_cur = Tracker.objects.filter(currency = 'test_cur').order_by('-timestamp_int')[:1]
	
	currencies = []
	currencies.append(test_cur[0])

	context = {
	'currencies' : currencies,
	'last_update' : test_cur[0].timestamp_str
	}
	
	#return HttpResponse("Index page")
	return render(request, 'tracker/index.html', context)
