from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import UniqueUsernameRegistrationForm
from .models import Product, Category, ShoppingCartItem,order_success 
from django.contrib import messages
from .forms import AuthenticationForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from django.shortcuts import render, redirect  
from django.db.models import F  
from .forms import CheckoutForm  
from .models import order_success, Product  




def register_view(request):
    if request.method == 'POST':
        form = UniqueUsernameRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UniqueUsernameRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    products = Product.objects.all().order_by('?')[:8]
    return render(request, 'home.html', {'products': products})

def public_home_view(request):
    products = Product.objects.all().order_by('?')[:8]
    return render(request, 'public_home.html', {'products': products})

def category_by_id_view(request, category_id):
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'products': products, 'category': category})

def category_by_name_view(request, category_name):
    try:
        category = Category.objects.get(分类名=category_name)
        products = category.products.all()
        return render(request, 'public_home.html', {'products': products})
    except Category.DoesNotExist:
        return HttpResponse("Category does not exist", status=404)

def home_category_by_name_view(request, category_name):
    try:
        category = Category.objects.get(分类名=category_name)
        products = category.products.all()
        return render(request, 'home.html', {'products': products})
    except Category.DoesNotExist:
        return HttpResponse("Category does not exist", status=404)


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


def add_to_cart(request, product_id):
    """
    添加商品到购物车
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        # 检查商品库存
        if product.产品库存 >= quantity:
            # 减少商品库存
            product.产品库存 -= quantity
            product.save()
            # 添加商品到购物车
            shopping_cart_item, created = ShoppingCartItem.objects.get_or_create(
                user=request.user,
                产品名称=product
            )
            if not created:
                shopping_cart_item.商品数量 += quantity
                shopping_cart_item.save()
            else:
                shopping_cart_item.商品数量 = quantity
                shopping_cart_item.save()
            return redirect('shopping_cart')
        else:
            # 库存不足，返回错误信息
            messages.error(request, '库存不足，无法添加商品到购物车。')
    # 如果是GET请求或者库存不足，则重定向到商品详情页面
    return redirect('product_detail', product_id=product_id)

def shopping_cart_view(request):
    """
    查看购物车
    """
    if request.method == 'GET':
        shopping_cart_items = ShoppingCartItem.objects.filter(user=request.user)
        # 计算购物车总价
        total_price = sum(item.产品名称.产品价格 * item.商品数量 for item in shopping_cart_items)
        
        context = {
            'shopping_cart_items': shopping_cart_items,
            'total_price': total_price
        }
        return render(request, 'shopping_cart.html', context)

# 销售
def checkout(request):  
    if request.method == 'POST':  
        form = CheckoutForm(request.POST)  
        if form.is_valid():  
            # 假设 shopping_cart_items 已经在 session 或者其他地方定义好了  
            shopping_cart_items = request.session.get('shopping_cart_items', [])  
            total_price = 0  
  
            for item in shopping_cart_items:  
                product = Product.objects.get(id=item['product_id'])  
                quantity = item['quantity']  
                  
                # 创建销售记录  
                order_success.objects.create(  
                    商品名称=product.产品名称,  
                    销售数量=quantity,  
                )  
                  
                # 更新商品库存  
                Product.objects.filter(id=product.id).update(产品库存=F('产品库存') - quantity)  
                  
                # 累加总价  
                total_price += product.产品价格 * quantity  
  
            # 清空购物车  
            request.session['shopping_cart_items'] = []  
              
            # 可以选择将总价等信息保存到订单中或者显示在感谢页面上  
  
            # 重定向到感谢页面或订单详情页面  
            return redirect('thank_you')  # 假设你有一个名为 'thank_you' 的URL  
    else:  
        form = CheckoutForm()  
  
    # 如果是GET请求，显示结算表单  
    return render(request, 'checkout.html', {'form': form})

def thank_you_view(request):  
    return render(request, 'thank_you.html')

def some_other_view(request):  
    # 处理逻辑...  
    # 当你想要重定向到感谢页面时  
    return redirect('thank_you')


