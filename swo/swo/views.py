from django.shortcuts import render
#import index.html file



def index(request):
    return render(request, 'index.html')