from django.shortcuts import render
from .models import appvariety

# Create your views here.
def all_apps(request):
    apps = appvariety.objects.all()
    return render(request, 'basicApp/all_app.html',{'apps': apps})