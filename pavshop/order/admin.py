from django.contrib import admin

from order.models import Checkout_billing, Shipping_Info, Payment_method

admin.site.register(Checkout_billing)
admin.site.register(Shipping_Info)
admin.site.register(Payment_method)

