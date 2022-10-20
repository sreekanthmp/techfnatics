
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from myapp.forms import Contactform, Imageform, Mediaform, Productform,Textform
from .models import Contact, Image, Products, Socialmedia,Text

def home(request):
    contacts=Contact.objects.all()
    product=Products.objects.all()
    images=Image.objects.all()
    medias=Socialmedia.objects.all()
    texts=Text.objects.all()
    jpg={
        'contacts':contacts,
        'product':product,
        'images':images,
        'medias':medias,
        'texts':texts
    }
    return render(request,'home.html',jpg)
    
@login_required()


def admin_view(request):

	return render(request, "admin_panel.html")

@login_required()


def contacts(request):
    if request.method=="POST":
        form=Contactform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('contacts')
    else:
        all_contact=Contact.objects.all()
    
        return render(request,"contact.html",{"all_contact":all_contact})

@login_required()

def delete_contact(request,id):
    contact=Contact.objects.get(pk=id)
    contact.delete()
    return redirect('contacts')
@login_required()

def update_contact(request,id):
    if request.method=="POST":
        contact=Contact.objects.get(pk=id)

        form=Contactform(request.POST or None, instance=contact)
        if form.is_valid():
            form.save()
        return redirect('contacts')
    else:
        all_contact=Contact.objects.get(pk=id)
    
        return render(request,"contact_update.html",{"all_contact":all_contact})
@login_required()
  
    
    
    
def products(request):
    if request.method=="POST":
        form=Productform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('products')
    else:
        form = Productform()
        all_product=Products.objects.all()
    
        return render(request,"product.html",{'form': form,"all_product":all_product})


@login_required()


def update_product(request,id):
    if request.method=="POST":
        product=Products.objects.get(pk=id)

        form=Productform(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
        return redirect('products')
    else:
        form = Productform()
        all_product=Products.objects.get(pk=id)
    
        return render(request,"product_update.html",{'form': form,"all_product":all_product})
@login_required()

def delete_product(request,id):
    product=Products.objects.get(pk=id)
    product.delete()
    return redirect('products')

@login_required()

def image(request):
    if request.method=="POST":
        form=Imageform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # img = form.instance
        # return render(request, 'product.html', {'form': form, 'img': img})    
        return redirect('image')
    else:
        form = Imageform()
        all_image=Image.objects.all()
    
        return render(request,"images.html",{'form': form,"all_image":all_image})
@login_required()

def update_image(request,id):
    if request.method=="POST":
        image=Image.objects.get(pk=id)

        form=Imageform(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
        return redirect('image')
    else:
        form = Imageform()
        all_image=Image.objects.get(pk=id)
        return render(request,"images_update.html",{'form': form,"all_image":all_image})
    
@login_required()
   
def delete_image(request,id):
    image=Image.objects.get(pk=id)
    image.delete()
    return redirect('image')



@login_required()


def medias(request):
    if request.method=="POST":
        form=Mediaform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('medias')
    else:
        form = Mediaform()

        all_link=Socialmedia.objects.all()
    
        return render(request,"socialmedia.html",{'form': form,"all_link":all_link})


    
    
    
    
@login_required()
 
def update_media(request,id):
    if request.method=="POST":
        media=Socialmedia.objects.get(pk=id)

        form=Mediaform(request.POST, request.FILES, instance=media)
        if form.is_valid():
            form.save()
        return redirect('medias')
    else:
        form = Mediaform()
        all_link=Socialmedia.objects.get(pk=id)
        return render(request,"socialmedia_update.html",{'form': form,"all_link":all_link})
    
@login_required()

    
def text(request):
    if request.method=="POST":
        form=Textform(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
        return redirect('text')
    else:
        form = Textform()
        all_text=Text.objects.all()
        return render(request,"text.html",{'form': form,"all_text":all_text})

    


    
def update_text(request,id):
    if request.method=="POST":
        media=Text.objects.get(pk=id)

        form=Textform(request.POST, request.FILES, instance=media)
        if form.is_valid():
            form.save()
        return redirect('text')
    else:
        form = Textform()
        all_link=Text.objects.get(pk=id)
        return render(request,"text_update.html",{'form': form,"all_link":all_link})
