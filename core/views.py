from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    



#Views
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username = form.cleaned_data['username'])
                if User.check_password(user, form.cleaned_data['password']):
                    pass
            except User.DoesNotExist:
                pass
    else:
        form = LoginForm()
        return render_to_response('core/login.html', {'form' : form}, context_instance=RequestContext(request))