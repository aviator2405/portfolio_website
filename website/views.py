from django.shortcuts import render,HttpResponse,redirect
from django.core.mail import send_mail,EmailMultiAlternatives
from website.models import feedback

# Create your views here.

def home(request):
    if request.method == 'POST':

        # fetching the data from the form 
        name= request.POST.get('name')
        email= request.POST.get('email')
        msg= request.POST.get('msg')

        # saving the data in the database
        data=feedback(name=name,email=email,message=msg)
        data.save()

        # terminal display of the fetch data 
        print (name)
        print (email)
        print (msg)

        # sending confirmation email to the user and the admin
        subject='CONFIRMATION MAIL'
        from_email = 'rohitportfolio24@gmail.com'
        to_email = [str(email),'rohitportfolio24@gmail.com']
        msg_body=f'<H1> Confirmation Mail </h1><br><br> <p>Thankyou for contacting <b>{name}</b> <br> I will attend you shortly. <br><br><br><b>Your Filled Details</b><br>Name- {name}<br><br>email- {email}<br><br>Your message- {msg}<br><br><br><b><i>Thanking You</i></b><br><br><br><b>Regards</b><br>Rohit Patel<br>rp240502@gmail.com<br>9039972014</p>'
        final_email=EmailMultiAlternatives(subject,msg_body,from_email,to_email)
        final_email.content_subtype='html'
        final_email.send()
        return render(request,"index.html",{"message":"Email Sent"})
    return render(request,'index.html',{"message":""})