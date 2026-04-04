from .models import Product

def categories_processor(request):
    return {
        'categories': Product.CATEGORY_CHOICES
    }