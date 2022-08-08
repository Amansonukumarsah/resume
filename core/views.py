from pickle import FALSE
from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def home(request):
  context = {'home': 'active'}
  return render(request, 'core/home.html', context)

def contact(request):
  if request.method=='POST':
    name=request.POST.get('Name')
    email=request.POST.get('Email'),
    subject=request.POST.get('Subject'),
    message=request.POST.get('Message')

    data={
      'name':name,
      'email':email,
      'subject':subject,
      'message':message
    }
    print(data)
    message=''' 
    New message:{}
    from:{}
    '''.format(data['message'],data['email'])
    send_mail(data['subject'],message,'',['amansonurn8@gmail.com'],fail_silently=FALSE)
  context = {'contact': 'active'}
  return render(request, 'core/contact.html', context)