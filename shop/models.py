from django.db import models

class OptionType(models.Model):
    name = models.CharField(max_length=100)  # np. Kolor marmuru

class OptionValue(models.Model):
    option_type = models.ForeignKey(OptionType, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)  # np. Zielony
    price_diff = models.DecimalField(max_digits=8, decimal_places=2, default=0)

class Product(models.Model):
    name = models.CharField(max_length=100)
    base_price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    options = models.ManyToManyField('OptionValue', blank=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    selected_options = models.ManyToManyField(OptionValue)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
