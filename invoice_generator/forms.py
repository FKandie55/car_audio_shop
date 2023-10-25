from django import forms
from .models import Invoice, InvoiceProduct

class NewInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer']

class CloseInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['is_closed']

class ReturnProductForm(forms.Form):
    invoice_number = forms.CharField(label="Invoice Number", max_length=20)
    model_number = forms.CharField(label="Model Number", max_length=20)
    quantity = forms.IntegerField(label="Quantity Returned")

class GenerateQuoteForm(forms.Form):
    model_number = forms.CharField(label="Model Number", max_length=20)
    quantity = forms.IntegerField(label="Quantity")

    def calculate_total(self):
        # Implement your logic to calculate the quote total here.
        # For example:
        model_number = self.cleaned_data['model_number']
        quantity = self.cleaned_data['quantity']
        # Fetch the product price from the database based on model_number and calculate the total.
        # total = price * quantity
        total = 0  # Replace with your logic
        return total
