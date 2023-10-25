from django.contrib import admin
from .models import Customer, Product, Invoice, InvoiceProduct

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'postal_code']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['model_number', 'price']

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'customer', 'is_closed']
    list_filter = ['is_closed']
    search_fields = ['invoice_number', 'customer__first_name', 'customer__last_name']

@admin.register(InvoiceProduct)
class InvoiceProductAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'product', 'quantity']

# Register any other models you have in your app, as needed.
