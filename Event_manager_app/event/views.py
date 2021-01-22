from django.shortcuts import render
from event.models import Event
import random
import array as arr
import datetime
from django.core.mail import send_mail
from django.contrib import messages

def form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        location = request.POST.get('loc')
        poster = request.POST.get('poster')
        start_date = request.POST.get('start_date')
        start_time = request.POST.get('start_time')
        end_date = request.POST.get('end_date')
        end_time = request.POST.get('end_time')
        last_date = request.POST.get('last_date')
        last_time = request.POST.get('last_time')
        email = request.POST.get('email')
        pswd = request.POST.get('pswd')
        obj = datetime.datetime.now()
    
        if not Event.objects.filter(email__exact=email,name__exact=name, start_date__exact=start_date,end_date__exact=end_date, start_time__exact=start_time, end_time__exact=end_time):
            data = Event(name=name, desc=desc, poster=poster, location=location, start_date=start_date, start_time=start_time, end_date=end_date, end_time=end_time, last_date=last_date, last_time=last_time, email=email, pswd=pswd)
            
            data.save()

            # For sending mail
            subject = "Event Registration successful"
            message = "".join(["Dear organizer,\nYour event have been registerd successfully.\n\nEvent details :\nEvent id : ", str(data.id), "\nEvent Name : ", str(data.name), "\n\nThank you for using our app."])
            send_mail(subject,message,"",[data.email], fail_silently=False)
            messages.success(request, 'Registration succesfull.')
        else :
            messages.error(request, "You have already registerd")
    return render(request, "event_form.html")
