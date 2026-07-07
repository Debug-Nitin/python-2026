from django.shortcuts import render
from .models import appvariety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_apps(request):
    apps = appvariety.objects.all()
    return render(request, 'basicApp/all_app.html',{'apps': apps})

def app_detail(request, app_id):
    app = get_object_or_404(appvariety, pk = app_id)
    return render(request, 'basicApp/app_detail.html',{'app': app})