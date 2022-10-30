from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .models import Info

# Create your views here.
def send_message(request):
    my_info = Info.objects.first()
    subject = request.POST['subject']
    email = request.POST.get('email')
    message = request.POST.get('message')
    
    
    if request.method == 'POST':
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )

     
    
    context = {'my_info':my_info}
    return render(request, 'contact/contact.html',context)