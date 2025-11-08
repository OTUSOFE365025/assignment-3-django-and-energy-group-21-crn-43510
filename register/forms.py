from django import forms # Import the forms library from Django

# Scans the form
class ScanForm(forms.Form):
    upc = forms.CharField(label='UPC', max_length=50)
