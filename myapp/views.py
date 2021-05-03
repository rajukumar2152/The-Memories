from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import*


def show_about_page(request):
    print("about page request")
    name = 'Learncodewith Durgesh'
    link = 'https://www.youtube.com/learncodewithduregsh'

    data = {
        'name': name,
        'link': link
    }

    return render(request, "about.html", data)


def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()

    # data = {'images': images, 'cats': cats}
    # data = {'cats': cats}
    # print(data)
    # print()
    # print(cats)
    # return render(request, "home.html", {'cats':cats} ,{'images':images})
    return render(request, "home.html",{'images':images ,'cats':cats})


def showcat(request ,cid):
    # print(cid)
   
    cats= Category.objects.all()

    category = Category.objects.get(pk=cid)
    # print(category)
    images = Image.objects.filter(cat=category)
    #  images = Image.objects.filter()
    # images = Image.objects.all()
    # print(cats)
    return render(request, "home.html", {'images': images, 'cats':cats})


def home(request):
    return redirect('/home')