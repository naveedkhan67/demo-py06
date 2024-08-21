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


usernames = ["naveed66", "naveed123", "naveed456", "naveed789", "naveed987", "naveed654", "naveed321", "naveed789", "naveed987", "naveed654", "naveed321"]


def list_usernames(request):
    colors = ["gray", "white"]
    return render(request, "list_usernames.html", {"usernames": usernames, "colors": colors})

articles = [
       {
           'id': 1,
           'title': 'Introduction to Django',
           'content': 'Django is a high-level Python web framework...',
           'author': 'Jane Doe',
           'published_date': '2023-08-21 10:30:00'
       },
       {
           'id': 2,
           'title': 'Understanding Django Templates',
           'content': 'Django templates allow you to dynamically generate HTML...',
           'author': 'John Smith',
           'published_date': '2023-08-22 14:45:00'
       },
       {
           'id': 3,
           'title': 'Django Views',
           'content': 'Django views is somthing detail detail.',
           'author': 'Naveed Khan',
           'published_date': '2023-08-23 14:45:00'
       },
       {
           'id': 4,
           'title': 'Variable Interpolation',
           'content': 'very intresting topic....',
           'author': 'sami ',
           'published_date': '2023-08-22 14:45:00'
       }
       
]

def articles_list(request):
    return render(request, "articles_list.html", context={"articles": articles})


def article_details(request, id):
    for article in articles:
        if article["id"] == id:
            return render(request, "articles_detail.html", article)
    
    return HttpResponse("Article not found")