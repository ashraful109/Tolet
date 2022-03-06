# from multiprocessing import context

from django.contrib import messages
from django.shortcuts import render
from django.core.paginator import Paginator
from home.models import House,Slider, Inquary
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
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
def post_rent_house(request):
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
        user = request.user

        House.objects.create(name=name,description=description,rent=rent,location=location,house_type=house_type,area=area,
        beds=beds,baths=baths,garage=garage,video=video,image=image,user=user) 
        messages.success(request, 'Property Added Successfully')
    else:
        return render(request, 'home/post_rent_house.html')
    return render(request, 'home/post_rent_house.html')

def inquary(request):
    if request.method=="POST":
        house_owner_email= request.POST.get('house_owner_email')
        house_id = request.POST.get('house_id')
        house_name = request.POST.get('house_name')


        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        user = request.user
        Inquary.objects.create(name=name,email=email,phone=phone,message=message)

        email_subject = 'Rent-House Inquary Message From Tolet'
        email_body = 'You Have an Inquary From '+name+'\n Email: '+email+'\nPhone:'+phone+'\nHe/She Send You This message:\n'+message+'\n\n For House ID:'+str(house_id)+'\nHouse Name:'+house_name+''
        email_address = house_owner_email

        email = EmailMessage(
            email_subject,
            email_body,
            'noreply@tolet.com',
            [email_address],   
        )
        email.send(fail_silently=False)

        messages.success(request, 'Inquary Send Successfully')
        return render(request, 'home/single_house.html')
    else:
        return render(request, 'home/single_house.html')
    # return render(request, 'home/single_house.html')
    
