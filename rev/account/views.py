from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, get_user_model
from django.contrib import messages

User=get_user_model()
def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('myapp:todo')
        else:
            messages.error(request, "Invalid email or password.")

    return render(request,"auth/login.html")

def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('username') 
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return redirect('account:signup')
        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = full_name 
            user.save()
            
            messages.success(request, "Account created! Please log in.")
            return redirect('account:login')
            
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('account:signup')

    return render(request,"auth/signup.html")

