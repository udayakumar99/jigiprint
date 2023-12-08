from django.shortcuts import render

# Create your views here.


def uday(request):
    data='u r promoted as CEO'
    
    return render(request,'uday.html',{'name':data})
def cond(request):
    return render(request,'if.html',{'a':50,'b':200,'c':90})