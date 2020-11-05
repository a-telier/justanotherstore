from django.shortcuts import render  #  renders HTML templates
from django.http import HttpResponse #  displays HttpResponse
# from products.models import Product

# obj = Product.objects.get(id=1)

product = {
    'category': 'category',
    'brand': 'brand',
    'line': 'line',
    'lineDescription': 'lineDescription',
    'product': 'product',
    'variant': 'variant',
    'productDescription': 'productDescription',
    'ingredients': 'ingredients',
    'price': 'price',
    'itemNo': 'itemNo',
    'image': 'image',
    'additionalImages': 'additionalImages'
}

#     'additionalImages': obj.additionalImages

# Here are the views that we created.
def homepage_view(request, *args, **kwargs):
    #   *args (Non Keyword Arguments)
    #   **kwargs (Keyword Arguments)
    #   Used as an argument when we are unsure about the number of arguments
    #   to pass in the functions
    #   print(args, kwargs)
    #   prints the user that has requested the page
    #   print(request.user)
    #   return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html") #, product)

def product_view(request, *args, **kwargs):
    return render(request, "product/detail.html")
