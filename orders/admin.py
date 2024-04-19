from django.contrib import admin
from orders.models import OrderProduct, Order


# Register your models here.

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    raw_id_fields = ("product",)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "status", )
    readonly_fields = ("created_at", "updated_at")
    inlines = [OrderProductInline]