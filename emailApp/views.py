from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse

def send_email(request):
    subject = 'Christmas Invitation'
    message = '''Hello Everyone, 
    This is to notify that you are invited to the Christmas event that is going to held on 25th December.
    Your presence will be appreciated.
    Thankyou !!!'''
    from_email = 'sabina@greentick.com.np'
    recipient_list = ['Beeplaw21@gmail.com']  

    send_mail(subject, message, from_email, recipient_list)

    return HttpResponse('Email sent successfully!')
