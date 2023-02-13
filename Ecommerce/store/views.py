from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,"store/index.html")

def collections(request):
    category =  category.objects.filter(status=0)
    context=