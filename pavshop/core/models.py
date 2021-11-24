from django.db import models

from pavshop.utils.base import BaseModel

class Contact_us(BaseModel):
    fullname = models.CharField(max_length=255, verbose_name="Fullname of the person")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=50, verbose_name="Phone number")
    subject = models.CharField(max_length=255, verbose_name="Subject")
    message = models.TextField(verbose_name="message")

    class Meta:
        verbose_name = "contact_us"
        verbose_name_plural = "contacts"
    
    def __str__(self) -> str:
        return self.fullname

class Subscribe(BaseModel):
    mail = models.EmailField(verbose_name="mail", unique=True)
    class Meta:
        verbose_name = "subscribe"
        verbose_name_plural = "subscribes"
    def __str__(self) -> str:
        return self.mail


# class Search(BaseModel):
#     search = models.TextField(max_length=255, verbose_name="Search")
#     user = models.ForeignKey('users.User', related_name="search", on_delete=models.CASCADE, verbose_name="User", null=True, blank=True)

#     class Meta:
#         verbose_name = "Search"
#         verbose_name_plural = "Searches"
    
#     def __str__(self) -> str:
#         return f'self.user'