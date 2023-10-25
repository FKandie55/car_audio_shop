from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Product, Invoice, InvoiceProduct
from .forms import NewInvoiceForm, CloseInvoiceForm, ReturnProductForm, GenerateQuoteForm

def create_invoice(request):
    if request.method == 'POST':
        form = NewInvoiceForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data['customer']
            new_invoice = Invoice(customer=customer)
            new_invoice.save()
            return redirect('invoice_created')
    else:
        form = NewInvoiceForm()
    return render(request, 'create_invoice.html', {'form': form})

def close_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    if request.method == 'POST':
        form = CloseInvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoice_closed')
    else:
        form = CloseInvoiceForm(instance=invoice)
    return render(request, 'close_invoice.html', {'form': form, 'invoice': invoice})

def return_product(request):
    if request.method == 'POST':
        form = ReturnProductForm(request.POST)
        if form.is_valid():
            invoice_number = form.cleaned_data['invoice_number']
            model_number = form.cleaned_data['model_number']
            quantity = form.cleaned_data['quantity']
            # Implement your logic for handling product returns here
            # For example, find the product in the invoice and update quantities.
            return redirect('product_returned')
    else:
        form = ReturnProductForm()
    return render(request, 'return_product.html', {'form': form})

def generate_quote(request):
    if request.method == 'POST':
        form = GenerateQuoteForm(request.POST)
        if form.is_valid():
            total = form.calculate_total()
            return render(request, 'generate_quote.html', {'form': form, 'total': total})
    else:
        form = GenerateQuoteForm()
    return render(request, 'generate_quote.html', {'form': form})
