from django.shortcuts import render
from django.core.mail import BadHeaderError,send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings


def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def service(request):
	return render(request, 'service.html')

def pricing(request):
	return render(request, 'pricing.html')


def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# mail
		if message_name and message_email and message:
			try:
				send_mail(message_name,message,message_email,['testmycode7@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return render(request, 'contact.html',{'message_name':message_name})
	else:
		return render(request, 'contact.html')


# def booking(request):
# 	if request.method == 'POST':
# 		your_name = request.POST['your-name']
# 		your_email = request.POST['your-email']
# 		your_address = request.POST['your-address']
# 		your_time = request.POST['your-time']
# 		your_message = request.POST['your-message']



def booking(request):
	if request.method == 'POST':
		your_name = request.POST['your-name']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_time = request.POST['your-time']
		your_message = request.POST['your-message']

		if your_name and your_message and your_email:
			try:
				send_mail(your_name, your_message, your_email,['testmycode7@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid Report')
			return render(request, 'booking.html', {'your_name':your_name})
	else:
		return render(request, 'booking.html')