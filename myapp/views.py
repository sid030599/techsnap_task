from distributed import Sub
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import smtplib as s


def homepage(request):
    

    if request.method == 'POST':
        
        ob = s.SMTP('smtp.gmail.com',587)
        ob1 = s.SMTP('smtp.gmail.com',587)

        ob.ehlo()
        ob.starttls()
        ob.login('sidqazwsx801@gmail.com','nxacvwwdcqjufjws')

        ob1.ehlo()
        ob1.starttls()
        ob1.login('shidharth030599@gmail.com','ajxhkboktrzbjyfz')


        sub = request.POST.get('subject')
        body = request.POST.get('message')
        emails = request.POST.get('mailone')
        
        message = "subject:{}\n\n{}".format(sub,body)
        
        lst = emails.split(",")
        
        

        ob.sendmail('sidqazwsx801@gmail.com',lst,message)
        ob1.sendmail('shidharth030599@gmail.com',lst,message)


        print('mail sent')
        ob.quit()
        ob1.quit()



        # sub = request.POST.get('subject')
        # message = request.POST.get('message')
        # email = request.POST.get('ema')
        # print(sub,message,email)
        # send_mail(sub,message,'setting.EMAIL_HOST_USER',[email],fail_silently=False)
        return render(request,'myapp/sent.html')

    
    return render(request,'myapp/homepage.html')
# Create your views here.
