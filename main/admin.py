from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active')
    list_filter = ('is_active', 'color')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    # readonly_fields = ('view',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'is_active')
    list_filter = ('is_active', 'category')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active','icon')
    list_filter = ('is_active',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ('image', 'is_active')
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'country', 'product_category', 'is_active', 'verified')
    list_filter = ('is_active', 'verified', 'recomended', 'country', 'product_category', 'color', 'created_at',)
    search_fields = ('name', 'desc', 'country')
    prepopulated_fields = {'slug': ('name',)}
    inlines = (ProductImageInline,)
    # readonly_fields = ('view',)



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
   
