import uuid # universely unique identifier
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from users.models import VendorProfile

from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator


class Category(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='category/thumbnail', blank=True)

    def __str__(self):
        return self.name

class CategoryImage(models.Model):
    category = models.ForeignKey(Category, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'category/covers/', blank=True)

    def __str__(self):
        return f'{self.category.name} cover id: {self.pk}'

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
    sku = models.PositiveIntegerField(default=5, verbose_name='Stock Keeping Unit')
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    slug = models.SlugField(blank=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True) #default=datetime.now() init

    def __str__(self):
        return f"{self.name} by {self.vendor.brand}"

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

# Slug generator signal
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)

# Review Model
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
