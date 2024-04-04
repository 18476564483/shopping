# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('commodity_app.urls')),  # 包含应用程序的 URL 配置
]
