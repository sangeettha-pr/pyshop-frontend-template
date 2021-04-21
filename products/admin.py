from django.contrib import admin
from .models import Product, Offer, Category


class OfferAdmin(admin.ModelAdmin):
    list_display=('code','discount')

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock')

class CategoryAdmin(admin.ModelAdmin):
    list_display= ('name',)

admin.site.register(Offer,OfferAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)

