from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(vat)
admin.site.register(product)
admin.site.register(priceHistory)
admin.site.register(order)
admin.site.register(transaction)