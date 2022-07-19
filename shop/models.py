from django.db import models
from django.urls import reverse

from clubs.models import Clubs


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Product(models.Model):
    JR = 'JR'
    YTH = 'YTH'
    SR = 'SR'
    SIZE_CHOICES = [(JR, 'junior'),
                    (YTH, 'youth'),
                    (SR, 'senior')]
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 related_name='products')
    club = models.ForeignKey(Clubs, on_delete=models.PROTECT, null=True, blank=True)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='store/%Y/%m/%d/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField()
    stock = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=(self.slug,))


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_absolute_url(self):
        return reverse('confirmation', args=(self.id,))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity

    def get_absolute_url(self):
        return reverse('confirmation', args=(self.id,))
