from django.contrib import admin
from django.utils.html import format_html
from product.models import Product, Product_version, Designer, Brand, Review, Shopping_card, Product_Category, ItemInShoppingCart, Images


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','discount','price','designer','brand','product_category')
    list_filter = ('brand', 'designer',)


class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ('product','get_image')
    list_filter = ['product']

    def get_image(self,obj):
        if obj.image:
            img = '<img src="{}" width="100" height="100" />'.format(obj.image.url)
            return format_html(img)
        return 'No Image'


class ShoppingCardAdmin(admin.ModelAdmin):
    list_display = ('user','is_ordered')
    list_editable = ('is_ordered',)
    



admin.site.register(Product, ProductAdmin)
admin.site.register(Product_version, ProductVersionAdmin)
admin.site.register(Designer)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(Shopping_card, ShoppingCardAdmin)
admin.site.register(Product_Category)
admin.site.register(ItemInShoppingCart)
admin.site.register(Images)