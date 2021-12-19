from django.contrib import admin
from .models import Product, OrderItem, Order, ColourVariation, SizeVariation, Address

# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address_type', 'address_line_1',
                    'address_line_2', 'zip_code', 'city']


admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(ColourVariation)
admin.site.register(SizeVariation)
admin.site.register(Address, AddressAdmin)
