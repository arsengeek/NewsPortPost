from django import forms
from django.contrib.auth.models import User, Group
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail,mail_admins
from ModalsDateBase.models import Author
        
class Signup(SignupForm):
    def save(self, request):
        author = Author.objects.create(user=request.user)
        author.save()
        
        send_mail (
            subject='Thanks for singup',
            message=f'Succes singup to user {author.username}',
            recipient_list=[author.email],
            from_email=None,
        )
        
        mail_admins(
            subject='New User',
            message=f'User {author.username} singup'
        )
        return author
    
    