from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')



def SignupPage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # Check if any field is empty
        if not uname or not email or not pass1 or not pass2:
            return HttpResponse("Please fill in all the fields.")

        # Check if passwords match
        if pass1 != pass2:
            return HttpResponse("Your Password and Confirm Password are not same!!")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            # return HttpResponse("User has been created suceessfully!!")
            return redirect('login')

            # print(uname,email,pass1,pass2)


    return render(request, 'signup.html')
    





def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')

        print(f'Username: {username}, Password: {pass1}')  # Debugging

        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            print(f'User authenticated: {user}')  # Debugging
            login(request, user)
            return redirect('home')  # Redirect to home page
        else:
            print('Login failed')  # Debugging
            return HttpResponse("Username and Password is incorrect!!")
    return render(request, 'login.html')



def LogoutPage(request):
    logout(request)
    return redirect('login')

