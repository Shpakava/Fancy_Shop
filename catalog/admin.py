from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Category

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # fields=["name", "stock", "is_available"]
    list_display = ["__str__", "name", "stock", "created_at"]
    readonly_fields = ["created_at", "get_image"] #поля только для чтения
    prepopulated_fields = {"slug": ("name",)} #предопределенные поля

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.pic.url} width="110" height="100">')

    get_image.short_description = "Image"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name",)}
