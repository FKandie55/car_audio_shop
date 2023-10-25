from django.urls import path
from . import views

app_name = 'invoice_generator'

urlpatterns = [
    path('create-invoice/', views.create_invoice, name='create_invoice'),
    path('close-invoice/<int:invoice_id>/', views.close_invoice, name='close_invoice'),
    path('return-product/', views.return_product, name='return_product'),
    path('generate-quote/', views.generate_quote, name='generate_quote'),
]
