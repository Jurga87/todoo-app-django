from django . shortcuts import render,redirect

def singup(request):
    return render (request,"singup.html")