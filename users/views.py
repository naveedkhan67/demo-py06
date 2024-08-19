from django.shortcuts import render, HttpResponse, redirect
# Create your views here.

def test_view(request):
    return HttpResponse("hello world")


def value_capture_test(request, name, age):
    return HttpResponse(f"This is my {name} and {age}")

def value_capture_test2(request, name, age):
    context = {
        "name": name, 
        "age": age,
        "default_c": "blue"
    }
    return render(request, "value.html", context)

credentials = {
    "username": "naveed66", 
    "password": "naveed123"

}


def login(request, username, password):
    
    if username == credentials["username"] and password == credentials["password"]:
        return redirect("/users/home/")
    else:
        return redirect("failure")


def home(request):
    return render(request, "home.html")

def failure(request):
    return render(request, "failure.html")
    