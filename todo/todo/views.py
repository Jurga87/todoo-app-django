from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import TODOO


def signup(request):
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
        User.objects.create_user(username=uname, email=email, password=pwd)

        return redirect("/loginn")

    return render(request, "singup.html")


def login_view(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")

        user = authenticate(request, username=uname, password=pwd)

        if user is not None:
            login(request, user)
            return redirect("/todo")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "loginn.html")

    return render(request, "loginn.html")


def todo(request):
    if request.method == "POST":
        title = request.POST.get("title")

        TODOO.objects.create(
            title=title,
            user=request.user
        )

        messages.success(request, f'Task "{title}" added successfully!')
        return redirect("/todo")

    # GET request → show list of todos
    todos = TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, "todo.html", {"todos": todos})

def edit_todo(request, srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        obj = TODOO.objects.get(srno=srno)
        obj.title = title
        obj.save()
        return redirect('/todo')

    obj = TODOO.objects.get(srno=srno)
    return render(request, 'edit_todo.html', {'obj': obj})