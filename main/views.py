from django.shortcuts import render, redirect
from django.core.mail import send_mail
from datetime import datetime

from django.template.loader import render_to_string

from main.models import *


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        if email:
            subscriber = Email.objects.filter(email=email)
            if not subscriber:
                subscriber = Email()
                subscriber.email = email
                subscriber.name = name
                subscriber.sent_at = datetime.now()
                subscriber.save()

        data = {
            'name': name,
            'email': email,
            'message': message,
        }
        print(data)
        html_content = render_to_string('./mail.html')
        send_mail(data['name'] + ", спасибо за подписку!", data['message'], '', [data['email']],
                  html_message=html_content)
        return redirect('/')
    return render(request, 'index.html')
