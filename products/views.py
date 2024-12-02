from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from .forms import ReviewForm

def home(request):
    return render(request, 'home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'products/product_detail.html', {'product': product, 'reviews': reviews, 'form': form})


def menu(request):
    # Define any data you want to pass to the template here
    return render(request, 'products/menu.html')