from django.shortcuts import render

from home.models import House,Slider

# Create your views here.
def home(request):
    slider = Slider.objects.all()
    house = House.objects.all()
    context = {
        'slider':slider,
        'house':house,
        

    }
    return render(request, 'home/index.html',context)