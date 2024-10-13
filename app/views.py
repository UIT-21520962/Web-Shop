from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import * 
from .models import Products
from .models import AdvertisingBanner
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from .models import SocialMediaLink
# Create your views here.

def home(request):
    products = Products.objects.all()

    # Truyền cả 'products' và 'banners' vào template
    context = {
        'products' : products,
    }   
    return render(request,'app/home.html', context)
    
 
def ProductOrders(request):
    if request.user.is_authenticated: 
        return render(request,'app/ProductOrders.html')
    else: 
        return render(request,'app/LoginForm.html')
    
       
def products_view(request):
    products = Products.objects.all()
    products1 = Products1.objects.all()
    products2 = Products2.objects.all()
    banners = AdvertisingBanner.objects.all()  # Lấy tất cả banner

    # Truyền cả 'products' và 'banners' vào template
    context = {
        'products' : products,
        'banners': banners,
        'products1' : products1,
        'products2' : products2,
    }

    return render(request, 'app/Products.html', context)

def products1_view(request):
    products1 = Products1.objects.all()
    banners = AdvertisingBanner.objects.all()  # Lấy tất cả banner

    # Truyền cả 'products' và 'banners' vào template
    context = {
        'banners': banners,
        'products1' : products1,
    }

    return render(request, 'app/Products1.html', context)

def products2_view(request):
    products2 = Products2.objects.all()
    banners = AdvertisingBanner.objects.all()  # Lấy tất cả banner

    # Truyền cả 'products' và 'banners' vào template
    context = {
        'banners': banners,
        'products2' : products2,
    }

    return render(request, 'app/Products2.html', context)



def LoginForm(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Tên người dùng hoặc mật khẩu không chính xác!')  # Thông báo lỗi
    
    return render(request, 'app/LoginForm.html')


def RegisterForm(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'app/RegisterForm.html', context)

def logout_view(request):
    logout(request)  # Đăng xuất người dùng
    return redirect('home')  # Điều hướng về trang đăng nhập

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Kiểm tra nếu mật khẩu và xác nhận mật khẩu khớp
        if password != confirm_password:
            messages.error(request, "Mật khẩu và xác nhận mật khẩu không khớp!")
            return render(request, 'app/RegisterForm.html')  # Trả lại form với thông báo lỗi

        # Kiểm tra nếu người dùng đã tồn tại
        if User.objects.filter(username=username).exists():
            messages.error(request, "Tên người dùng đã tồn tại!")
            return render(request, 'app/RegisterForm.html')

        # Tạo người dùng nếu mọi thứ đều hợp lệ
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Đăng ký thành công!")
        return redirect('login')  # Redirect đến trang đăng nhập

    return render(request, 'app/RegisterForm.html')  # Trả lại form nếu không phải POST


def ProductOrders(request):
    # Lấy tất cả các mạng xã hội từ model
    social_media = SocialMediaLink.objects.all()
    return render(request, 'app/ProductOrders.html', {'social_media': social_media})

@login_required
def admin_view(request):
    is_admin = request.user.is_staff or request.user.is_superuser
    return render(request, 'admin', {'is_admin': is_admin})

