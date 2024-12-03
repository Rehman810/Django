from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render, redirect
from .models import User 

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # user = User.objects.get(phonenumber=phonenumber)
            user = User.objects.get(username=username)
            if password==user.password:
            # if check_password(password, user.password):
                return render(request, 'login/result.html',{'username':username})  
            else:
                return render(request, 'login/login.html', {'error': 'Invalid credentials.'})
        except User.DoesNotExist:
            return render(request, 'login/login.html', {'error': 'User does not exist.'})

    return render(request, 'login/login.html')


from django.shortcuts import render
from .models import User  # Ensure the User model is correctly imported

from django.shortcuts import render
from .models import User  # Ensure the User model is correctly imported

def forgetpassword(request):
    if request.method == "POST":
        phonenumber = request.POST.get('phone')

        try:
            # Check if the phone number exists in the User model
            user = User.objects.get(phonenumber=phonenumber)
            account_info={'username': user.username,'password': user.password}
            # Pass user details to the result page
            return render(request, 'login/forgetresult.html', {'account_info':account_info})

        except User.DoesNotExist:
            # Render the same page with an error message if phone number is not found
            return render(request, 'login/ForgetPassword.html', {'error': 'Phone number not found.'})

    # Render the form for GET requests
    return render(request, 'login/ForgetPassword.html')



def registration(request):
    
    if request.method == "POST":

        username = request.POST.get('username')
        phonenumber = request.POST.get('phonenumber')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if the passwords match
        if password != confirm_password:
            return render(request, 'login/Registration.html', {'error': 'Passwords do not match.'})

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'login/Registration.html', {'error': 'Username already exists.'})
        # Check if the username already exists
        if User.objects.filter(phonenumber=phonenumber).exists():
            return render(request, 'login/Registration.html', {'error': 'This phonenumber is used'})

        # hashed_password = make_password(password)

        # Save user to the database
        User.objects.create(username=username, phonenumber=phonenumber, password=password)
        # User.objects.create(username=username, phonenumber=phonenumber, password=hashed_password)

        # Redirect to the login page after successful registration
        return redirect('home')  # Replace 'login' with your actual login URL name

    return render(request, 'login/registration.html')


# def forgetpassword(request):
#     return render(request,'login\Forgetpassword.html')
def home(request):
    return render(request, 'login\home.html') 
def result(request):
    return render(request,'login\Result.html')


