from django.shortcuts import render,redirect
from.models import Book
from django.contrib.auth import authenticate,login

def customer(request):
    return render(request,"customer.html")
def librarian(request):
    return render(request,"librarian.html")
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or homepage
            return redirect('librarian.html')
        else:
            # Return an error message or render the login page again
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

    
def register(request):
    return render(request,"register.html")



