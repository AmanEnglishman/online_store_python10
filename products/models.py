from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories',
    )

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
    )
    stock = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    discount = models.ForeignKey(
        'Discount',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products'
    )

    def get_discounted_price(self):
        if self.discount and self.discount.active:
            now = timezone.now()
            if self.discount.start_date <= now <= self.discount.end_date:
                return self.price * (100 - self.discount.percent) / 100
        return self.price


    def __str__(self):
        return f'{self.name}'

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.ImageField(upload_to='images/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'Image for {self.product.name}'

class ProductSpecification(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.name

from django.contrib.auth.models import User

class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} review for {self.product.name}'


class Discount(models.Model):
    name = models.CharField(max_length=255)
    percent = models.PositiveSmallIntegerField(help_text="Скидка в процентах")
    active = models.BooleanField(default=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.percent}%"


class Banner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banners/')
    url = models.URLField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title