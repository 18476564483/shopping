from django.db import models
from django.contrib.auth.models import User

# 分类管理
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    分类名 = models.CharField(max_length=100, verbose_name='分类名')

    class Meta:
        db_table = 'category'
        verbose_name = '分类管理'
        verbose_name_plural = '分类管理'

    def __str__(self):
        return self.分类名

# 商品模型
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    产品名称 = models.CharField(max_length=100)
    产品描述 = models.TextField()
    产品价格 = models.DecimalField(max_digits=10, decimal_places=2)
    产品库存 = models.PositiveIntegerField(default=0)
    产品所属类别 = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    创建日期 = models.DateTimeField(auto_now_add=True)
    # 产品图片 = models.ImageField(upload_to='products/', null=True, blank=True)

    class Meta:
        db_table = 'product'
        verbose_name = '产品模型'
        verbose_name_plural = '产品模型'

    def __str__(self):
        return self.产品名称

# 购物车模型
class ShoppingCart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopping_carts')
    创建日期 = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shoppingcart'
        verbose_name = '购物车模型'
        verbose_name_plural = '购物车模型'

    def __str__(self):
        return f"购物车-{self.id}"

# 产品详情模型
class ProductDetail(models.Model):
    id = models.AutoField(primary_key=True)
    产品详情 = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='details')
    详情描述 = models.TextField()
    详情图片 = models.ImageField(upload_to='shopping/shop/commodity_app/static/images/')
    创建日期 = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'productdetail'
        verbose_name = '产品详情模型'
        verbose_name_plural = '产品详情模型'

    def __str__(self):
        return f"{self.产品详情.产品名称}'s details"

# 购物车条目模型
class ShoppingCartItem(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopping_cart_items')  # 购物车条目所属的用户
    产品名称 = models.ForeignKey(Product, on_delete=models.CASCADE)  # 购物车中的商品
    商品数量 = models.PositiveIntegerField(default=1)  # 商品数量，默认为1

    class Meta:
        db_table = 'shopping_cart_item'
        verbose_name = '购物车条目'
        verbose_name_plural = '购物车条目'

    def __str__(self):
        return f"{self.商品数量} - {self.产品名称}"  # 修改了这里的返回值，将数量放在前面
    
    # 销售模型
class order_success(models.Model):
    id = models.AutoField(primary_key=True)
    商品名称 = models.CharField(max_length=100)  # 销售的商品名称
    销售数量 = models.PositiveIntegerField()  # 销售的商品数量
    销售日期 = models.DateTimeField(auto_now_add=True)  # 销售日期，默认为当前时间

    class Meta:
        db_table = 'order_success'
        verbose_name = '销售记录'
        verbose_name_plural = '销售记录'

    def __str__(self):
        return f"{self.商品名称} - {self.销售数量}件 - {self.销售日期}"
