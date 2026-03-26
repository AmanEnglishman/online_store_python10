from django.contrib import admin

from .models import Product, Category, ProductImage, ProductSpecification, Review, Discount


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)
    list_filter = ('parent',)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price',)
    search_fields = ('name', 'description',)
    list_filter = ('category', 'created_at',)

    inlines = [ProductImageInline, ProductSpecificationInline]

    readonly_fields = ('created_at',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', )

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', )