from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Headphone)
admin.site.register(Earphone)
admin.site.register(Speaker)
admin.site.register(Order)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)
