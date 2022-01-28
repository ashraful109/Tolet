from django.shortcuts import render

from home.models import Slider

# Create your views here.
def home(request):
    slider = Slider.objects.all()
    context = {
        'slider':slider
    }
    return render(request, 'home/index.html',context)