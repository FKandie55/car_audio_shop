from django.contrib import admin
from .models import Customer, Product, Invoice, InvoiceProduct

class InvoiceProductInline(admin.TabularInline):
    model = InvoiceProduct
    extra = 1

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'postal_code', 'amount_paid']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['model_number', 'product_name', 'price']

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'customer', 'created_at', 'is_closed']
    list_filter = ['is_closed']
    search_fields = ['invoice_number', 'customer__first_name', 'customer__last_name']
    inlines = [InvoiceProductInline]

@admin.register(InvoiceProduct)
class InvoiceProductAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'product', 'quantity']

# Register other models as needed.
