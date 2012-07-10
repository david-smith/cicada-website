from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def landing_page(request):
    return render_to_response('backend/landing_page.html', {}, context_instance = RequestContext(request))