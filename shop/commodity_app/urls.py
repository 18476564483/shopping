from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_view, name='register'),  # 注册页面路由
    path('login/', views.login_view, name='login'),  # 登录页面路由
    path('logout/', views.logout_view, name='logout'),  # 注销路由
    path('', views.home_view, name='home'),  # 个人主页路由
    path('public/', views.public_home_view, name='public_home'),  # 公共主页路由
    path('category/<int:category_id>/', views.category_by_id_view, name='category_view_by_id'),  # 分类页面路由
    path('category/<str:category_name>/', views.category_by_name_view, name='category_view_by_name'),  # 分类页面路由
    path('home/<str:category_name>/', views.home_category_by_name_view, name='home_category_by_name'),  # 分类页面路由
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),  # 商品详情路由
    path('shopping_cart/', views.shopping_cart_view, name='shopping_cart'),  # 购物车路由
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),  # 添加到购物车路由
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # 添加到购物车路由
    path('checkout/', views.checkout, name='checkout'), 
    path('thank-you/', views.thank_you_view, name='thank_you'), 
    
]
