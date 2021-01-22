from django.shortcuts import render,HttpResponse
from event.models import Event
from participate.models import Participate

# Create your views here.

def index(request):
    if request.method == "POST":
        event_id = request.POST.get('id')
        pswd = request.POST.get('pswd')
        obj = Event.objects.filter(id__exact=event_id)
        if obj:
            if obj[0].pswd == pswd:
                details = list(Participate.objects.filter(event__exact=obj[0].name))
                length = len(details)
                return render(request, 'participate_list.html', {'length':length, 'participate_details':details})
        else:
            return render(request, 'dashboard.html')
    return render(request, 'dashboard.html')