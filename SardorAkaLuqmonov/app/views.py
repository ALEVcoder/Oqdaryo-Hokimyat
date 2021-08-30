from django.shortcuts import render
from django.core.mail import send_mail
from .models import *
# Create your views here.
def home(request):
    hokimnews = news.objects.all()

    if request.method == 'POST':
        ism = request.POST['user']
        familya = request.POST['last']
        xabar = request.POST['xabar']
        local = request.POST['local']
        email = request.POST['pochta']
        title=ism
        msg='Sizga '+ism+'dan xabar bor'+'\nFamilyasi: '+familya+'\nTelfon raqami: '+email+ ' \n Manzili:  '+ local +'\nXABAR Mazmuni:\n'+xabar

        print(ism, xabar, email)
        send_mail(
            ism,
            msg,
            email,
            ['alevcoder1@gmail.com'],
            fail_silently=False,
        )
        
        print('Xabaringiz ketti')
    return render(request, 'index.html', {'news':hokimnews})