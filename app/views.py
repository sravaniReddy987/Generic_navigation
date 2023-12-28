from django.shortcuts import render

# Create your views here.
def gf(request):
    return render(request,'gf.html')
def bf(request):
    return render(request,'bf.html')
