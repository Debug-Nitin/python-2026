from django.shortcuts import render

# Create your views here.
def all_apps(request):
    return render(request, 'basicApp/all_app.html')