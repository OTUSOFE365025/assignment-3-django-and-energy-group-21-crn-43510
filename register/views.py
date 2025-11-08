from django.shortcuts import render
from .models import Product
from .forms import ScanForm

# Load the product from the database
def load_products(request):
    Product.objects.all().delete()
    sample_products = [
        ("012345678905", "Banana (each)", 0.39),
        ("012345678906", "Milk 1L", 2.49),
        ("012345678907", "White Bread", 1.79),
        ("111111111111", "Apple", 0.99),
        ("222222222222", "Eggs (Dozen)", 3.49),
    ]
    for upc, name, price in sample_products:
        Product.objects.create(upc=upc, name=name, price=price)
    return render(request, "scan.html", {"form": ScanForm(), "loaded": True})

# Scan the product
def scan(request):
    product = None
    searched_upc = None

    if request.method == "POST":
        form = ScanForm(request.POST)
        if form.is_valid():
            searched_upc = form.cleaned_data["upc"]
            try:
                product = Product.objects.get(upc=searched_upc)
            except Product.DoesNotExist:
                product = None
    else:
        form = ScanForm()

    return render(request, "scan.html", {
        "form": form,
        "product": product,
        "searched_upc": searched_upc,
    })
