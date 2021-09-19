from django.shortcuts import redirect, render
from django.core.mail import send_mail




def Emailsendview(request):
    send_mail('Django-EmailSender','Thank You for Registrations!!!!',
            'bobadesp1234@gmail.com',['bobadesp1234@gmail.com'],fail_silently=False,)
    return redirect('home')

def Homeview(request):
    template_name='Home.html'
    return render(request,template_name)