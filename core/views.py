from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django import forms
from django.contrib.auth import authenticate, login, logout

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    



#Views
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/tracker')
                else:
                    return render_to_response('core/login.html', {'form' : form, 'error' : 'Account not active'}, 
                                              context_instance=RequestContext(request))
            else:
                return render_to_response('core/login.html', {'form' : form, 'error' : 'Username or password was incorrect'}, 
                                          context_instance=RequestContext(request))
        else:
            return render_to_response('core/login.html', {'form' : form, 'error' : 'Form not valid'}, 
                                          context_instance=RequestContext(request))       
    else:
        form = LoginForm()
        return render_to_response('core/login.html', {'form' : form}, context_instance=RequestContext(request))
    
def logout_view(request):
    logout(request)
    return redirect('/')