# Event Manager Web Application 
### This is my project on Event Manager web application through which One can register for an event and participant can register for that event. There the facility for the Event organisers to get the all details about the participants registered for their event which needs authentication to see the details.


#### Project Components :
1) Home page - link to the other sites. E.g. Event Registration, Participant Registration, Event Dashboard
2) Event Registration - Organiser can register for an event using this site.
3) Participant Registration - Participant can register for an event using this site.
4) Event Dashboard - Organiser can see the Partipants details which have created by them. Authentication required Event ID (which is unique for all events and created by Django backend) and password which hae used at the time of registering the Event.
5) The message will be displayed on Event/Participant Registration site for successful registration and warning message in case of already registered.

#### Notifications:
1) Organiser will get an Email notification on successfully registered for the event.
2) Participant will get Email and Message notification about their successful Registration.

#### Hiding Authentication details:
Since I have implemented the Emial and Message notification, so it's necessary to hide my details. So, I have created .env file to hide the details and there is one .env.example file which is copy of my .env file. Via putting the Email and Twilio Accounts' authentiction details in .env.example approprietly, one can enable Email and Message notifictions.

#### Front-end:
Front-end is created using HTML, CSS and Javascript only and it's a responsive website.

#### Demo Video of Web Application:
[click here](https://drive.google.com/file/d/1ewh6_7YtXH5vg_JSMX6JJmjt3PKt9nwn/view?usp=sharing)
