from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Product
from django.utils.html import format_html


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'display_image', 'location']

    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
    
admin.site.register(CustomUser, UserAdmin)  
admin.site.register(Product)
