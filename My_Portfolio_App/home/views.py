from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("This is my home page")
    return render(request,'home.html')

def about(request):
    #return HttpResponse("This is my  about page")
    return render(request,'about.html')

def skills(request):
    #return HttpResponse("This is my  about page")
    return render(request,'skills.html')

def projects(request):
    #return HttpResponse("This is my projects page")
    return render(request,'projects.html')


def contact(request):
    #return HttpResponse("This is my contact page")
    return render(request,'contact.html')
