from django.contrib import admin
from .models import Product, OptionType, OptionValue, Order

admin.site.register(Product)
admin.site.register(OptionType)
admin.site.register(OptionValue)
admin.site.register(Order)
