from common.shortcuts import render_response
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def landing_page(request):
    return render_response(request, 'backend/landing_page.html', {})