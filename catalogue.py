"""Manages product catalogue operations."""

def display_products(catalogue):
    for product in catalogue:
        print(product)

def search_category(catalogue, category):
    for product in catalogue:
        if product[1].lower() == category.lower():
            print(product)

