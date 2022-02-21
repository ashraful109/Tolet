# from multiprocessing import context
from django.shortcuts import render
from django.core.paginator import Paginator
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

def all_house(request):
    house_list = House.objects.all()
    paginator = Paginator(house_list,3)
    page_number = request.GET.get('page')
    house = paginator.get_page(page_number)
    context = {
        'house': house,

    }
    return render(request, 'home/all_house.html',context)

def single_house(request,id):
    house = House.objects.get(id=id)
    context = {
        'house':house
    }
    return render(request, 'home/single_house.html',context)

def contact(request):
    return render(request, 'home/contact.html')