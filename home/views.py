# from multiprocessing import context

from django.contrib import messages
from django.shortcuts import render
from django.core.paginator import Paginator
from home.models import House,Slider
from django.contrib.auth.decorators import login_required
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
    house_list = House.objects.filter(is_publish=True)
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

@login_required
def post_house(request):
    if request.method=="POST" and request.FILES['image']:
        name = request.POST.get('name')
        description = request.POST.get('description')
        rent = request.POST.get('rent')
        location = request.POST.get('location')
        house_type = request.POST.get('house_type')
        area = request.POST.get('area')
        beds = request.POST.get('beds')
        baths = request.POST.get('baths')
        garage = request.POST.get('garage')
        video = request.POST.get('video')
        image = request.FILES['image']

        House.objects.create(name=name,description=description,rent=rent,location=location,house_type=house_type,area=area,
        beds=beds,baths=baths,garage=garage,video=video,image=image) 
        messages.success(request, 'Property Added Successfully')
    else:
        return render(request, 'home/post_rent_house.html')
    return render(request, 'home/post_rent_house.html')