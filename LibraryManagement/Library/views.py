from django.shortcuts import render, HttpResponse, redirect
from .models import admin1, book
# Create your views here.


# Home Page
def index(request):
    return render(request,"index.html")


# Admin Registration Page
def signup(request):
    if request.method=="POST":
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        password=request.POST["password"]
        app=admin1(fname=fname,lname=lname,email=email,password=password)
        app.save()
        return redirect('/login_page')
    else:
        return HttpResponse("Registration Failed")


# Admin Login Page
def login_page(request):
    return render(request,"login_page.html")


# Verify Admin credentials, create session and redirect to dashboard
def login_check(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        data = admin1.objects.all().filter(email=email,password=password)
        if data:
            request.session['username']=email
            return redirect('/dashboard')
        else:
            return redirect('/login_page')


# Dashboard can only be accessed if logged in
def dashboard(request):
    if request.session.get("username") is not None:
        data=book.objects.all()
        return render(request,"dashboard.html",{'data':data})
    else:
        return redirect('/login_page')


# logout and redirect to login page
def logout(request):
    del request.session['username']
    return redirect('/login_page')


# Add a new book page
def add_book(request):
    if request.session.get("username") is not None:
        return render(request,"add_book.html")
    else:
        return redirect('/login_page')


# Adding the book details in the database
def adding_book(request):
    if request.method=="POST":
        bname=request.POST["bname"]
        aname=request.POST["aname"]
        price=request.POST["price"]
        app=book(bname=bname,aname=aname,price=price)
        app.save()
        return redirect('/dashboard')
    else:
        return HttpResponse("Failed")


# delete a book record
def delete_book(request):
    id=request.GET['id']
    book.objects.filter(id=id).delete()
    return redirect('/dashboard')


# Edit a book detail page
def edit_book(request):
    if request.session.get("username") is not None:
        id=request.GET["id"]
        data=book.objects.all().filter(id=id)
        return render(request,"edit_book.html",{'data':data})
    else:
        return redirect('/login_page')


# Update the book values in the database
def update_book(request):
    if request.method=="POST":
        id=request.POST["id"]
        bname=request.POST["bname"]
        aname=request.POST["aname"]
        price=request.POST["price"]
        book.objects.filter(id=id).update(bname=bname,aname=aname,price=price)
        return redirect('/dashboard')
    else:
        return redirect('/dashboard')




