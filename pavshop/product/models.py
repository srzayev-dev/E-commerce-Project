from django.db import models
from pavshop.utils.base import BaseModel

class Product(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Title of the product")
    discount = models.IntegerField(verbose_name="Discount", null=True, blank=True)
    price = models.DecimalField(verbose_name="Price", decimal_places=2, max_digits=10)
    designer = models.ForeignKey("Designer", on_delete=models.SET_NULL, related_name="product_design", null=True, blank=True, verbose_name="Designer")
    brand = models.ForeignKey("Brand", on_delete=models.SET_NULL, related_name="Brand", null=True, blank=True, verbose_name="Brand")
    mini_description = models.TextField(max_length=255, verbose_name="Description minimum")
    full_description = models.TextField(verbose_name="Full Description")
    info = models.TextField(verbose_name="Product Information")
    info_delivery = models.TextField(verbose_name="Delivery Information")
    product_category = models.ForeignKey("product.Product_Category", verbose_name="Product Category", on_delete=models.CASCADE, related_name="Category", null=True, blank=True)


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    
    @property
    def main_version(self):
        return self.versions.filter(is_main=True).first()
    
    

    @property
    def total_quantity(self):
        return sum([version.quantity for version in self.versions.all()])
    

    
    def __str__(self) -> str:
        return self.title



class Designer(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Title of the Designer")

    class Meta:
        verbose_name = "Designer"
        verbose_name_plural = "Designers"
    
    def __str__(self) -> str:
        return self.title


class Brand(BaseModel):
    title = models.CharField(verbose_name="Title of the Brand", max_length=255)
    

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
    
    def __str__(self) -> str:
        return self.title


class Product_version(BaseModel):
    size = models.CharField(max_length=10, verbose_name="Size of the product")
    color = models.CharField(verbose_name="Color", max_length=30)
    quantity = models.IntegerField(verbose_name="Quantity", default=0)
    image = models.ImageField(verbose_name="Image", null=True, blank=True, upload_to = 'products/image/')
    is_main = models.BooleanField(verbose_name="Is Main?", default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="versions", verbose_name="Product")


    class Meta:
        verbose_name = "Product_version"
        verbose_name_plural = "Product_versions"
    
    # @property
    # def images(self):
    #     return self.product_version.all()
    
        # versions.filter(is_main=True).first()
    
    def __str__(self) -> str:
        return f'{self.product} - {self.color} - {self.size}'

class Images(BaseModel):
    image = models.ImageField(verbose_name="Image", upload_to = 'products/image/')
    product_version = models.ForeignKey(Product_version, on_delete=models.CASCADE, related_name="product_version", verbose_name="Version", null=True, blank=True)
  
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
    
    def __str__(self) -> str:
        return f'{self.product_version}'


class Review(BaseModel):
    name = models.CharField(max_length=255, verbose_name='name',null=True, blank=True, default="")
    review = models.TextField(max_length=255, verbose_name="Review of the Product")
    email = models.EmailField(verbose_name="Email",null=True, blank=True, default="")
    user = models.ForeignKey('users.User', related_name="reviewsOfProduct", on_delete=models.CASCADE, verbose_name="User", null=True, blank=True)
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="review", verbose_name="Product")

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
    
    def __str__(self) -> str:
        return self.email


class Shopping_card(BaseModel):
    products = models.ManyToManyField(
        Product, verbose_name="Products in shopping card", related_name="shopping_cards")
    user = models.ForeignKey(
        'users.User', 
        verbose_name="Which User's shopping card?",
        related_name="shoppingCardOfUser",
        on_delete=models.CASCADE, null=True, blank=True 
    )
    is_ordered = models.BooleanField(verbose_name="Is ordered?", default=False)
    shipping_address = models.ForeignKey('order.Shipping_Info', related_name="shipaddress", on_delete=models.CASCADE, verbose_name="Shipping Address", null=True, blank=True)

    class Meta:
        verbose_name = "Shopping card"
        verbose_name_plural = "Shopping cards"
    
    def __str__(self):
        return f'{self.user}'

    
class ItemInShoppingCart(BaseModel):
    quantity = models.IntegerField(verbose_name="Quantity", default=0)
    userOfShoppingCard = models.ForeignKey(Shopping_card,  related_name="usersOfShoppingCard", on_delete=models.CASCADE, verbose_name="user", null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="productOfShoppingCard", verbose_name="Product", null=True, blank=True)

    class Meta:
        verbose_name = "ShoppingCardItem"
        verbose_name_plural = "ShoppingCardItems"

    def __str__(self):
        return f'{self.userOfShoppingCard}'

class Product_Category(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Category name")

    class Meta:
        verbose_name = "Product_category"
        verbose_name_plural = "Product_categories"

    def __str__(self):
        return f'{self.title}'