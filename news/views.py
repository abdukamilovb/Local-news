from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout




def index(request):
    return render(request, 'home.html')


# def signup(request):
#     return render(request, 'signup.html')  # signup.html sahifasini qaytarish



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import CustomUser

def signup(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Parollar bir xil ekanligini tekshiramiz
        if password != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Username va email unikal ekanligini tekshiramiz
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!")
            return redirect('signup')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('signup')

        # Yangi foydalanuvchini yaratamiz
        user = CustomUser.objects.create(
            username=username,
            email=email,
            phone=phone,
            first_name=full_name,
            password=make_password(password)  # Parolni shifrlaymiz
        )
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('signin')

    return render(request, "signup.html")



from django.contrib.auth import authenticate, login

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Foydalanuvchini tekshirish
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("user")  # Muvaffaqiyatli kirgandan keyin bosh sahifaga yo‘naltirish
        else:
            messages.error(request, "Incorrect username or password!")
            return redirect("signin")

    return render(request, "signin.html")




def user_logout(request):
    logout(request)
    return redirect("signin")  # Chiqishdan keyin signin sahifasiga qaytarish



@login_required
def user_page(request):
    return render(request, "user.html")







from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser

@login_required
def custom_admin(request):
    users = CustomUser.objects.all()
    return render(request, 'admin.html', {'users': users})

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.lavozimi = request.POST.get("lavozimi")
        user.is_active = "is_active" in request.POST
        user.is_staff = "is_staff" in request.POST
        user.save()
        return redirect('custom_admin')

    return render(request, 'edit_user.html', {'user': user})
