from django.http import HttpResponse
import datetime

def hello(request):
	return HttpResponse("Hello world!")

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>new is %s.</body></html>" %now

	return HttpResponse(html)
def hour_ahead(request,offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>new is %s.</body></html>" %dt

	return HttpResponse(html)
	

