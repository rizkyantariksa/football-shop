from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):

    context = {
        'npm' : '2406495552',
        'name': request.user.username,
        'class': 'PBP B',
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
       'form': form
    }

    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, uuid=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'uuid': str(product.uuid),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'brand': product.brand,
            'stock': product.stock,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_uuid):
   try:
    product_item = Product.objects.filter(uuid=product_uuid)
    xml_data = serializers.serialize("xml", product_item)
    return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
      return HttpResponse(status=404)
      
def show_json_by_id(request, product_uuid):
    try:
        product = Product.objects.select_related('user').get(uuid=product_uuid)
        data = {
            'uuid': str(product.uuid),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'brand': product.brand,
            'stock': product.stock,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, uuid=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, uuid=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'
    brand = request.POST.get("brand")
    stock = request.POST.get("stock")
    user = request.user

    new_product = Product(
        name=name,
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        brand=brand,
        stock=stock,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@require_POST
def edit_product_ajax(request, id):
    product = get_object_or_404(Product, uuid=id)
    
    # Check if user owns this product
    if product.user != request.user:
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)
    
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'
    brand = request.POST.get("brand")
    stock = request.POST.get("stock")
    
    product.name = name
    product.price = price
    product.description = description
    product.category = category
    product.thumbnail = thumbnail
    product.is_featured = is_featured
    product.brand = brand
    product.stock = stock
    product.save()
    
    return JsonResponse({'success': True, 'message': 'Product updated successfully'})

@require_POST
def delete_product_ajax(request, id):
    product = get_object_or_404(Product, uuid=id)
    
    # Check if user owns this product
    if product.user != request.user:
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)
    
    product.delete()
    return JsonResponse({'success': True, 'message': 'Product deleted successfully'})

@require_POST
def login_ajax(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return JsonResponse({
            'success': True,
            'message': 'Login successful',
            'redirect': reverse('main:show_main')
        })
    else:
        return JsonResponse({
            'success': False,
            'error': 'Invalid username or password'
        }, status=401)

@require_POST
def register_ajax(request):
    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    
    # Validation
    if not username or not password1 or not password2:
        return JsonResponse({
            'success': False,
            'error': 'All fields are required'
        }, status=400)
    
    if password1 != password2:
        return JsonResponse({
            'success': False,
            'error': 'Passwords do not match'
        }, status=400)
    
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            'success': False,
            'error': 'Username already exists'
        }, status=400)

    try:
        temp_user = User(username=username)
        validate_password(password1, user=temp_user)
    except ValidationError as e:
        return JsonResponse({
            'success': False,
            'error': ' '.join(e.messages)
        }, status=400)
    
    # Create user
    try:
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        return JsonResponse({
            'success': True,
            'message': 'Account created successfully',
            'redirect': reverse('main:login')
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)
    
def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = strip_tags(data.get("name", ""))  # Strip HTML tags
        description = strip_tags(data.get("description", ""))  # Strip HTML tags
        category = data.get("category", "")
        price = data.get("price", "")
        stock = data.get("stock", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)
        user = request.user
        
        new_product = Product(
            name=name, 
            description=description,
            category=category,
            price=price,
            stock=stock,
            thumbnail=thumbnail,
            is_featured=is_featured,
            user=user
        )
        new_product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@login_required
def show_my_products_json(request):
    products = Product.objects.filter(user=request.user)
    
    data = []
    for product in products:
        data.append({
            'uuid': str(product.uuid),
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'thumbnail': product.thumbnail or '',
            'category': product.category,
            'brand': product.brand,
            'stock': product.stock,
            'is_featured': product.is_featured,
            'created_at': product.created_at.isoformat(),
            'user_id': product.user.id,
        })
    
    return JsonResponse(data, safe=False)