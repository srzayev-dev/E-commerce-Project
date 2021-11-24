import re
from unicodedata import decimal

from django.contrib.auth import get_user_model
from django.core import mail
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers
from blog.models import Blog, Blog_Category
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from core.models import Subscribe
 
from product.models import Product_Category, Product
from api.serializers import ProductSerializer, Product_categorySerializer, BlogSerializer, Blog_categorySerializer, UserLoginSerializer, UserSerializer, CardItemSerializer, SubscribeSerializer

from django.contrib.auth import login

from rest_framework.authtoken.serializers import AuthTokenSerializer


class LoginAPI(GenericAPIView):
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        user_serializer = UserSerializer(user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_detail': user_serializer.data
        })

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from product.models import Product_Category, Product, Product_version, Shopping_card, ItemInShoppingCart
from api.serializers import ProductSerializer, ProductVersionSerializer, RegistrationSerializers, CardSerializer



class ProductAPIView(APIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            obj = Product.objects.get(pk=kwargs.get('pk'))
            serializer = self.serializer_class(obj)
        else:
            qs = Product.objects.all()
            serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create_product(self, data):
        return Product.objects.create(
            title = data.get('title'),
            discount = int(data.get('discount')),
            price = data.get('price'),
            designer = data.get('product_design'),
            brand = data.get('Brand'),
            mini_description = data.get('mini_description'),
            full_description = data.get('full_description'),
            info = data.get('info'),
            info_delivery = data.get('info_delivery'),
            product_category = data.get('Product.product_category')
        )
    
    def create_product_versions(self, data):
        product = self.create_product(data)
        print(type(product))
        versions = []
        for version in data.get('versions'):
            version = Product_version(**version)
            version.product = product
            versions.append(version)
        Product_version.objects.bulk_create(versions)
        return product
    
    def post(self, request, *args, **kwargs):
        data = request.data
        product = self.create_product_versions(data)
        serializer = self.serializer_class(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProductVersionAPIView(APIView):
    serializer = ProductVersionSerializer
    def get(self, request, *args, **kwargs):
        if kwargs.get('product_id'):
            obj = Product_version.objects.filter(product__id=kwargs.get('product_id'))
            stat = status.HTTP_200_OK
            result = self.serializer(obj, many=True).data
            if kwargs.get('pk'):
                obj = Product_version.objects.get(pk=kwargs.get('pk'))
                result = self.serializer(obj).data
        else:
            stat = status.HTTP_404_NOT_FOUND
            result = {'detail' : 'Product not exist.'}
        return Response(result, status=stat)





class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = RegistrationSerializers


class CardView(APIView):
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        basket = Shopping_card.objects.get_or_create(user=request.user, is_ordered=False)   
        serializer = self.serializer_class(request.user.shoppingCardOfUser)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        qt = request.data.get('product_qty')
        product_id = request.data.get('product_id')
        action = request.data.get('action')
        product = Product.objects.filter(pk=product_id).first()
        serializer = ProductSerializer(product)
        print(product,'salaaam')
        if product:
            basket = Shopping_card.objects.get_or_create(user=request.user, is_ordered=False)
            if action == 'add':
                print("action is add")
                ItemInShoppingCart.objects.get_or_create(userOfShoppingCard=Shopping_card.objects.get(user=request.user, is_ordered=False), product=product)
                item = ItemInShoppingCart.objects.get(userOfShoppingCard=Shopping_card.objects.get(user=request.user, is_ordered=False), product=product)
                quant = item.quantity
                quant+=int(qt)
                ItemInShoppingCart.objects.filter(userOfShoppingCard=Shopping_card.objects.get(user=request.user, is_ordered=False), product=product).update(quantity=quant)
                sebet = ItemInShoppingCart.objects.filter(userOfShoppingCard=Shopping_card.objects.get(user=request.user, is_ordered=False))
                arr = []
                for i in sebet:
                    sebetSerizalier = CardItemSerializer(i)
                    arr.append(sebetSerizalier.data)
                Shopping_card.objects.get(user=request.user, is_ordered=False).products.add(product)
                message = {'success': True, 'message' : 'Product added to your card.'}
                return Response(arr, status=status.HTTP_201_CREATED)
            elif action == "update":
                print("action is update")
                ItemInShoppingCart.objects.get_or_create(userOfShoppingCard=Shopping_card.objects.get(user=request.user, is_ordered=False), product=product)
                item = ItemInShoppingCart.objects.get(userOfShoppingCard=Shopping_card.objects.get(user=request.user, is_ordered=False), product=product)
                quant = item.quantity
                quant=int(qt)
                ItemInShoppingCart.objects.filter(userOfShoppingCard=Shopping_card.objects.get(user=request.user, is_ordered=False), product=product).update(quantity=quant)
                sebet = ItemInShoppingCart.objects.filter(userOfShoppingCard=Shopping_card.objects.get(user=request.user, is_ordered=False))
                arr = []
                for i in sebet:
                    sebetSerizalier = CardItemSerializer(i)
                    arr.append(sebetSerizalier.data)
                Shopping_card.objects.get(user=request.user, is_ordered=False).products.add(product)
                message = {'success': True, 'message' : 'Product added to your card.'}
                return Response(arr, status=status.HTTP_201_CREATED)
            else:
                print("action is remove")
                ItemInShoppingCart.objects.get_or_create(userOfShoppingCard=Shopping_card.objects.get(user=request.user, is_ordered=False), product=product)
                item = ItemInShoppingCart.objects.get(userOfShoppingCard=Shopping_card.objects.get(user=request.user, is_ordered=False), product=product)
                quant = 0
                quant=int(qt)
                ItemInShoppingCart.objects.filter(userOfShoppingCard=Shopping_card.objects.get(user=request.user, is_ordered=False), product=product).update(quantity=quant)
                sebet = ItemInShoppingCart.objects.filter(userOfShoppingCard=Shopping_card.objects.get(user=request.user, is_ordered=False))
                arr = []
                for i in sebet:
                    sebetSerizalier = CardItemSerializer(i)
                    arr.append(sebetSerizalier.data)
                Shopping_card.objects.get(user=request.user, is_ordered=False).products.remove(product)
                ItemInShoppingCart.objects.filter(userOfShoppingCard=Shopping_card.objects.get(user=request.user, is_ordered=False), product=product).delete()
                message = {'success': True, 'message' : 'Product added to your card.'}
                return Response(arr, status=status.HTTP_201_CREATED)
        message = {'success': False, 'message' : 'Product not found.'}
        return Response( serializer.data,status=status.HTTP_400_BAD_REQUEST)

class ItemCardView(APIView):
    serializer_class = CardItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        basket = Shopping_card.objects.get_or_create(user=request.user, is_ordered=False)
        obj = ItemInShoppingCart.objects.filter(userOfShoppingCard=Shopping_card.objects.get(user=request.user, is_ordered=False))
        serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class SingleProductAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListBlogAPIView(ListAPIView):
    """This endpoint list all of the available Blogs from the database"""
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CreateBlogAPIView(CreateAPIView):
    """TThis endpoint allows for creation of a Blog"""
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class UpdateBlogAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Blog by passing in the id of the Blog to update"""
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class DeleteBlogAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Blog from the database"""
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class SingleBlogAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = BlogSerializer

class ListBlogCategoryAPIView(ListAPIView):
    """This endpoint list all of the available Blog_category from the database"""
    queryset = Blog_Category.objects.all()
    serializer_class = Blog_categorySerializer

class CreateBlogCategoryAPIView(CreateAPIView):
    """TThis endpoint allows for creation of a Blog_category"""
    queryset = Blog_Category.objects.all()
    serializer_class = Blog_categorySerializer

class UpdateBlogCategoryAPIView(UpdateAPIView):
    """TThis endpoint allows for creation of a Blog_category"""
    queryset = Blog_Category.objects.all()
    serializer_class = Blog_categorySerializer

class DeleteBlogCategoryAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Blog_category from the database"""
    queryset = Blog_Category.objects.all()
    serializer_class = Blog_categorySerializer

class ListProductCategoryAPIView(ListAPIView):
    """This endpoint list all of the available Product_category from the database"""
    queryset = Product_Category.objects.all()
    serializer_class = Product_categorySerializer

class CreateProductCategoryAPIView(CreateAPIView):
    """TThis endpoint allows for creation of a Product_category"""
    queryset = Product_Category.objects.all()
    serializer_class = Product_categorySerializer

class UpdateProductCategoryAPIView(UpdateAPIView):
    """TThis endpoint allows for creation of a Product_category"""
    queryset = Product_Category.objects.all()
    serializer_class = Product_categorySerializer

class DeleteProductCategoryAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Product_category from the database"""
    queryset = Product_Category.objects.all()
    serializer_class = Product_categorySerializer




class ListShoppingCardAPIView(ListAPIView):
    queryset = Shopping_card.objects.all()
    serializer_class = CardSerializer

class SubscriberAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SubscribeSerializer()  # create a serializer
        mail =  request.data['mail']
        subscribe = Subscribe(
            mail = mail
        )
        subscribe.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    