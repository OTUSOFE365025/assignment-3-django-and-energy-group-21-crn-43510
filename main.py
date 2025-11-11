############################################################################
## Django ORM Standalone Python Template
############################################################################

import sys
sys.dont_write_bytecode = True

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

import django
django.setup()

from db.models import Product

############################################################################
## START OF APPLICATION
############################################################################

# Populate database
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

print("Database seeded with products.\n")

# Cash register scanning loop
while True:
    upc = input("Scan UPC (or type 'exit'): ").strip()

    if upc.lower() == "exit":
        print("Exiting cash register.")
        break

    try:
        product = Product.objects.get(upc=upc)
        print(f"Product: {product.name} | Price: ${product.price}\n")
    except Product.DoesNotExist:
        print("Product not found.\n")
