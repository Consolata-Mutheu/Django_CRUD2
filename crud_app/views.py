
from django.shortcuts import render,redirect, get_object_or_404

from .models import  Item

# Create your views here.

#CRUD
#create code
def create_item(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        description=request.get('description')

        Item.objects.create(name=name, description=description)
        return redirect('item_list')
    return render(request,'item_form.html')


#read
def item_list(request):
    items = Item.objects.all()
    return render(request,'item_list.html',{'items':items})


#update
def update_item(request,pk):
    item = get_object_or_404(Item,pk=pk)
    if request.method == 'POST':
        item.name=request.POST.get('name')
        item.description=request.POST.get('description')
        item.save()
        return redirect('item_list')
    return render(request,'item_form.html',{'item':item})

#delete Logic
def delete_item(request,pk):
    item = get_object_or_404(Item,pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request,'item_confirm_delete.html',{'item':item})