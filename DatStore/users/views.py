from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model ,login, logout, authenticate
from django.contrib import messages
from DatStore.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User


from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.shortcuts import redirect

from .mails import Mail

from django.contrib.auth.models import Group

from .forms import UserRegistrationForm,UserUpdateForm

from django.db import models
from django.core.signals import request_finished
from django.dispatch import receiver

def activate(request, uidb64, token):
    User= get_user_model()
    try:
        uid= force_str(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
    except:
        user= None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Gracias por su confirmación por correo electrónico. Ahora puede iniciar sesión en su cuenta.')
        return redirect('login')
    else:
        messages.error(request, 'Link de activación inválido')
    return redirect('index')


def activateEmail(request, user, to_email):
    mail_subject="Activa tu cuenta de usuario"
    message= render_to_string("template_activate_account.html",{
        'user':user.username,
        'domain': get_current_site(request).domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request,f'Querido {user}, por favor ve a tu email {to_email} y checa tu inbox.')
    else:
        message.error(request,f'Problema al enviar el email {to_email}')



def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form= UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=False
            user.save()
            group = Group.objects.get(name='Clientes')
            user.groups.add(group)
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('index')
        else:
            for error in list(form.errors.values()):

                messages.error(request, error)
    else:
        form=UserRegistrationForm()

    return render(
        request=request,
        template_name= 'users/register.html', 
        context={'form': form}
    )

@receiver(models.signals.post_save, sender=User)
def post_save_user_signal_handler(sender, instance, created, **kwargs):
    if created:
       group = Group.objects.get(name='Clientes')
       instance.groups.add(group)
       instance.save()

def profile(request, username):
    if request.method == "POST":
        user= request.user
        forms = form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            messages.success(request, f'{user_form.username}, se ha actualizado tu perfil')
            return redirect('users:profile', user_form.username)
        
        for error in list(form.errors.values()):

                messages.error(request, error)

        
    user=get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        return render(
            request=request,
            template_name= 'users/profile.html', 
            context={'form': form}
            )
    return redirect('')