from django.shortcuts import render_to_response, redirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from common.shortcuts import render_response

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
                    return render_response(request, 'core/login.html', {'form' : form, 'error' : 'Account not active'})
            else:
                return render_response(request, 'core/login.html', {'form' : form, 'error' : 'Username or password was incorrect'})
        else:
            return render_response(request, 'core/login.html', {'form' : form, 'error' : 'Form not valid'})
    else:
        form = LoginForm()
        return render_response(request, 'core/login.html', {'form' : form})
    
def logout_view(request):
    logout(request)
    return redirect('/')

def weather(request):
    import urllib2
    response = urllib2.urlopen("http://partner.metoffice.gov.uk/public/val/wxfcs/all/json/352478?res=daily&key=96b521e9-dd99-4e2c-9816-61dd6581d50f")
    response_data = response.read()
    return render_to_response('weather.html', {'data': response_data}, mimetype='application/json');
    