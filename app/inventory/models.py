from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=55,unique=True)
    is_active = models.BooleanField(default=True)
    level = models.SmallIntegerField()
    #self refering foreign key for subcategories
    parent = models.ForeignKey('self', on_delete=models.RESTRICT, blank=True, null=True, related_name='subcategories')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PromotionEvent(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ProductPromotionEvent(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    promotion_event = models.ForeignKey(PromotionEvent, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name} - {self.promotion_event.name}"

    class Meta:
        unique_together = ('product', 'promotion_event')

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class StockManagement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    last_checked_at = models.DateTimeField()

    def __str__(self):
        return f"{self.product.name} - {self.quantity} in stock"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username} on {self.order_date.strftime('%Y-%m-%d %H:%M:%S')}"
    

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='order_products')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_products')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('order', 'product')

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"