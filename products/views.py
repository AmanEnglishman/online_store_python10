from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg


from .models import Product
from .forms import ReviewForm, Review

def index(request):
    products = Product.objects.prefetch_related('images').all()[:12]
    return render(request, 'index.html', {'products': products})

def contacts(request):
    return render(request, 'contacts.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all().order_by('-created_at')

    avg_rating = reviews.aggregate(avg=Avg('rating'))['avg'] or 0
    avg_rating = round(avg_rating)

    if request.method == 'POST':
        if request.user.is_authenticated:


            # if Review.objects.filter(user=request.user, product=product).exists():
            #     return redirect('product_detail', pk=pk)

            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.product = product
                review.save()
                return redirect('product_detail', pk=pk)
        else:
            return redirect('login')
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
        'avg_rating': avg_rating,
        'specifications': product.productspecification_set.all(),
    }

    return render(request, 'product_detail.html', context)