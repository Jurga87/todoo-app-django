from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def singup(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")

        # Check if username already exists
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists.")
            return render(request, "singup.html")

        # Check if email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, "singup.html")

        # Create new user
        my_user = User.objects.create_user(username=uname, email=email, password=pwd)
        my_user.save()

        # Redirect to login page after successful signup
        return redirect("/loginn")

    # Render signup page for GET request
    return render(request, "singup.html")

def login_view(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        print(uname, pwd)
        
        # Authenticate user
        user = authenticate(request, username=uname, password=pwd)

        if user is not None:
            login(request, user)
            return redirect("/todopage")  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "loginn.html")
    return render(request, "loginn.html")