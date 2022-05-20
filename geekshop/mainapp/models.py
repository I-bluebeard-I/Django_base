from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=64,
        unique=True
    )
    description = models.TextField(
        verbose_name='description',
        blank=True
    )

    is_active = models.BooleanField(
        verbose_name='active',
        default=True
    )


    def __str__(self):
        return f'{self.id} - {self.name}'


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='name',
        max_length=128
    )
    image = models.ImageField(
        verbose_name='image',
        upload_to='products',
        blank=True
    )
    short_desc = models.CharField(
        verbose_name='short_description',
        max_length=128,
        blank=True
    )
    description = models.TextField(
        verbose_name='description',
        blank=True
    )
    price = models.DecimalField(
        verbose_name='price',
        max_digits=8,
        decimal_places=2,
        default=0
    )
    quantity = models.PositiveIntegerField(
        verbose_name='quantity',
        default=0
    )
    is_active = models.BooleanField(
        verbose_name='active',
        default=True
    )


    def __str__(self):
        return f'{self.name} ({self.category.name})'
