from django.template.loader import get_template

from django.core.mail import EmailMultiAlternatives

from django.conf import settings

from .tokens import account_activation_token

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render



class Mail:

   @staticmethod
   def send_complete_order(orden, user,request):
    subject ='Activa tu Usuario'
    template= get_template('users/correodiseno.html')
    content=template.render({
        'user':user.username,
        'domain': get_current_site(request).domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
   
    message= EmailMultiAlternatives(subject,
    'Compras',
    settings.EMAIL_HOST_USER,
    [user.email])

    message.attach_alternative(content, 'text/html')

    message.send()