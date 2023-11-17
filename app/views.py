from django.shortcuts import render

# Create your views here.

def ifstatement(request):
    data = {'a':10, 'b':20}
    d= {'compare': data}
    return render (request,'ifstatement.html',context = data)

def ifelse(request):
    data = {'d':100, 'e':20, 'f':300}
    d= {'compare': data}
    return render (request,'ifelse.html',context = data)

def ifelif(request):
    data = {'g':10, 'h':20, 'i':30}
    d= {'compare': data}
    return render (request,'ifelif.html',context = data)

def nested(request):
    data = {'x':10, 'y':200, 'z':3000}
    d= {'compare': data}
    return render (request,'nested.html',context = data)
