import uuid # universely unique identifier
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from users.models import VendorProfile


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    vendor = models.ForeignKey(
        VendorProfile,
        on_delete=models.CASCADE,
        default=None
    )
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    ) # my_note: this can be manytomany ->will update later
    product_cover = models.ImageField(upload_to='product_covers/', blank=True)

    def __str__(self):
        return f"{self.name} by {self.vendor.brand}"

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.CharField(max_length=255)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user.username}:{self.review}" 
