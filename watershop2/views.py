from django.shortcuts import render
from django.http import HttpResponse
from .app.forms import CallbackForm
from django.http import HttpRequest,HttpResponseRedirect,JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def about(request):
    return render(request, "about.html")


def links(request):
    return render(request, "links.html")


def pool(request:HttpRequest):
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            # return JsonResponse{"true":True}
            return render(request, "pool.html",{"result":form.cleaned_data})
            # return HttpResponseRedirect("/about/")
    else:
        form = CallbackForm()
    return render(request, "pool.html",{"form":form})
