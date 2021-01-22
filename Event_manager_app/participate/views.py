from django.shortcuts import render,redirect
from event.models import Event
from participate.models import Participate
from datetime import datetime
from django.core.mail import send_mail
import os
from twilio.rest import Client
from django.contrib import messages
from decouple import config

# Create your views here.

def form(request):
    today = datetime.now()
    date = str(today.date())
    time = str(today.time())
    events = Event.objects.filter(last_date__gte=date).exclude(last_date__exact=date, last_time__lte=time)

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        if(len(contact) == 10):
            contact = '+91'+contact
        event= request.POST.get('event')
        lst = list(event.split(' '))
        event_name = lst[0]
        event_id = lst[1][1:-1]

        event_details = Event.objects.get(id__exact=event_id)
        isContact = Participate.objects.filter(contact__exact=contact)
        isEmail = Participate.objects.filter(email__exact=email)
       
        if not(isContact or isEmail):
            print('1')
            if request.POST.get('isGroup') == '1':
                data = Participate(name=name, event=event_name, contact=contact, email=email, no_of_people='1')
                data.save()
            else :
                no_of_people = request.POST.get('no_of_people')
                data = Participate(name=name, event=event_name, contact=contact, email=email, no_of_people=no_of_people)
                data.save()

            subject = "Registration successful"
            message = "".join(["Dear enthusist,\nYour registration for the event ", str(event_details.name)," is successfully done.\n\nYour Registration details :\nYour id : ", str(data.id), "\nYour Name : ", str(data.name), "\nContact No :", str(data.contact), "\n\nEvent details : \nEvent Name : ", str(event_details.name), "\nVenue :", str(event_details.location), "\nTime : From ", str(datetime.strftime(event_details.start_date,'%d-%m-%y')), " at ", str(event_details.start_time),"\n            To ", str(datetime.strftime(event_details.end_date,'%d-%m-%y')), " upto ", str(event_details.end_time),"\nNo. of participates Registered : ", str(data.no_of_people),"\n\nSee you on the event venue."])
            send_mail(subject, message, "", [data.email], fail_silently=False)

            account_sid = config('TWILIO_SID')
            auth_token = config('TWILIO_AUTH_TOKEN')
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body="".join(["Dear enthusist,\nYour registration for the event ", str(event_details.name)," is successfully done.\n\nYour Registration details :\nYour id : ", str(data.id), "\nYour Name : ", str(data.name), "\nEamil ID :", str(data.email), "\n\nEvent details : \nEvent Name : ", str(event_details.name), "\nVenue :", str(event_details.location), "\n\nTime :\nFrom ", str(datetime.strftime(event_details.start_date,'%d-%m-%y')), " at ", str(event_details.start_time),"\nTo ", str(datetime.strftime(event_details.end_date,'%d-%m-%y')), " upto ", str(event_details.end_time),"\nNo. of participates Registered : ", str(data.no_of_people),"\n\nSee you on the event venue."]),
                from_=config('TWILIO_NUM'),
                to=contact
            )

            messages.success(request, 'Registration succesfull.')
        else :
            messages.error(request, "You have already registerd")
    return render(request, "participate_form.html", {"up_events":events})
