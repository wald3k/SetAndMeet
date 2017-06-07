from django.shortcuts import render

import datetime #for datetime.now()
# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def email(request):
    if request.method == 'GET':
        initial = {'from_email':''}
        if(request.user.is_authenticated()):
            initial['from_email'] = request.user.email
        form = ContactForm(initial) #passing dict to a constructor. Dict keys are named as form fields.
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            category = form.cleaned_data['category']
            print category
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            admin_mailbox = ['SetAndMeet@gmail.com']
            try:
                send_mail(category + " " + subject, message, from_email, admin_mailbox)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})

def success(request):
     return render(request, "email_success.html")

def _print_to_console(subject, from_email, message, admin_mailbox):
	''' Private function to print a message 
		call it like: _print_to_console(...)  #print result to console 
	'''
	print "*** NEW MESSAGE HAS BEEN SENT ***"
	print "Date: " 		+ str(datetime.datetime.now())
	print "From: " 		+ from_email
	print "To: "      	+ str(admin_mailbox) #convert list to string
	print "Subject: "	+ subject
	print "Body: "		+ message
	print "*********************************"
