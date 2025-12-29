from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

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
        return redirect("login")

    # Render signup page for GET request
    return render(request, "singup.html")