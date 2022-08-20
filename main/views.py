
from queue import Empty
from django.http import HttpResponseNotFound,HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from . import models
from .forms import Emailc
# Create your views here.

def main(request):
    Offrs = []
    banner2 = models.Image_trend_2.objects.all()
    banner = models.image_u.objects.first()
    category = models.category.objects.all()
    product_all = models.Product.objects.all()
    sabad = models.sabad.objects.count()
    ino = models.interest.objects.count()
    saba = models.sabad.objects.all()
    brands = models.Brand.objects.all()
    
    for e in models.Product.objects.all():
        if e.price_offer != None:
            
            
            Offrs += models.Product.objects.filter(name= e)
    if request.method == "POST":
        form = Emailc(request.POST)
        if form.is_valid():
            email=models.Email()
            email.Email = form.cleaned_data['Email']
            if models.Email.objects.get(Email=email.Email):
                messages.warning(request,"فرمت ایمیل درست نیست یا قبلا ثبت شده")
            else:
                email.save()
                messages.success(request,"شما عضو خبرنامه شدی")

    else:
        form = Emailc()
    
    return render(request,
    "index.html",
    {"data_banner":banner2,"ofpr":Offrs,
    "category":category,"allp":product_all,
    "banner":banner,"brand":brands,"form":form,
    "ino":ino,"sabad":sabad,
    "saba":saba})



def search(request):
    if request.method == "POST":
        print("ok")

def sabadolikes(request):
    models.sabad.objects.all()
    models.interest.objects.all()
    pass
def likes(request,id):
    if request.user.is_authenticated:
        pro = models.Product.objects.get(id=id)
        a = request.user.id
        models.interest.objects.create(id_user=a,id_pro=pro.id)
        return redirect("/likes")
    else:
        messages.info(request,"شما عضو سایت نشدید")
        return redirect('/')
def sabad(request,id=0):
    if request.method == "POST":
        if request.user.is_authenticated:
            id_use = request.user.id
            t = 0
            try:
                pro = models.Product.objects.get(id=id)
                a = request.user.id
                if request.POST['T']:
                    t =request.POST['T']      
                models.sabad.objects.create(id_user=a,id_pro=pro.id,T=t)
                if models.jamsabad.objects.get(id_user=a):
                    pass
                else:
                    models.jamsabad.objects.create(id_user=a)

                return redirect('../')
            except:
                if models.sabad.objects.get(id_pro=id) == True:
                    return redirect("/sabad")

        sabad = models.sabad.objects.count()
        ino = models.interest.objects.count()
        saba = models.sabad.objects.all()
        category = models.category.objects.all()
        product_all = models.Product.objects.all()
        if request.user.is_authenticated:
            id_use = request.user.id
        else:
            id_use = 0
        return render(request,"sabad.html",{"ino":ino,"sabad":sabad,"saba":saba,"category":category,"allp":product_all,"id_use":id_use})

    #         try:
    #         except:
    #     else:
    #         messages.info(request,"شما عوض سایت نشدید")
    #         return redirect('../')
    # sabad = models.sabad.objects.count()
    # ino = models.interest.objects.count()
    # saba = models.sabad.objects.all()
    # category = models.category.objects.all()
    # product_all = models.Product.objects.all()
    # if request.user.is_authenticated:
    #     id_use = request.user.id
    # else:
    #     id_use = 0
    # return render(request,"sabad.html",{"ino":ino,"sabad":sabad,"saba":saba,"category":category,"allp":product_all,"id_use":id_use})