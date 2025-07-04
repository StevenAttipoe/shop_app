from django.contrib import admin
from .models import (
    Category, Product, PromotionEvent, ProductPromotionEvent, 
    User, StockManagement, Order, OrderProduct
)

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(PromotionEvent)
admin.site.register(ProductPromotionEvent)
admin.site.register(User)
admin.site.register(StockManagement)
admin.site.register(Order)
admin.site.register(OrderProduct)