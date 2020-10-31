from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Clothes,Electronics,Utencils,Beauty_Products
# Create your views here.
def shop(request):
    clothes = Clothes.objects.all()
    electr = Electronics.objects.all()
    uten = Utencils.objects.all()

    if request.method == 'POST':
        if 'btn' in request.POST:
            etitle = request.POST.get('etitle')
            edesc = request.POST.get('edesc')
            eimg = request.FILES.get('eimg')
            eprice = request.POST.get('eprice')

            data = Clothes(title = etitle, desc=edesc,image = eimg, price=eprice)
            data.save()
            messages.success(request, "Clothes Item Added Successfully")

        elif 'btn1' in request.POST:
            etitle1 = request.POST.get('etitle1')
            edesc1 = request.POST.get('edesc1')
            eimg1 = request.FILES.get('eimg1')
            eprice1= request.POST.get('eprice1')

            data1 = Electronics(title = etitle1, desc=edesc1,image = eimg1, price=eprice1)
            data1.save()
            messages.success(request, "Electronics Item Added Successfully")

        elif 'btn2' in request.POST:
            etitle2 = request.POST.get('etitle2')
            edesc2 = request.POST.get('edesc2')
            eimg2 = request.FILES.get('eimg2')
            eprice2 = request.POST.get('eprice2')

            data2 = Utencils(title = etitle2, desc=edesc2,image = eimg2, price=eprice2)
            data2.save()
            messages.success(request, "Utencils Item Added Successfully")

    return render(request, 'ecomm_home.html',{'ecomm':clothes,'ecomm1':electr,'ecomm2':uten})

def delete(request, id=id):
    
    item_delete=Clothes.objects.get(id=id)
    item_delete.delete()
    messages.success(request, "One Item From Clothes Deleted Successfully")
    return redirect('shop')

def delete1(request, id):
    item_delete1=Electronics.objects.get(id=id)
    item_delete1.delete()
    messages.success(request, "One Item From Electronics Deleted Successfully")
    return redirect('shop')

def delete2(request, id):
    item_delete2=Utencils.objects.get(id=id)
    item_delete2.delete()
    messages.success(request, "One Item From Utencils Deleted Successfully")
    return redirect('shop')

def viewitem(request, id):
    viewitem1=Clothes.objects.get(id=id)
    
    return render(request, 'viewitem.html',{'view1':viewitem1})

def viewitem1(request,id):
    viewitem2=Electronics.objects.get(id=id)
    
    return render(request, 'viewitem.html',{'view2':viewitem2})

def viewitem2(request,id):
    viewitem3=Utencils.objects.get(id=id)

    return render(request, 'viewitem.html',{'view3':viewitem3})