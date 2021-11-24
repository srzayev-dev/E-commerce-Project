from django.db.models import fields
from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.models import Subscribe

from users.models import User
from django.db.models import fields
from blog.models import Blog, Blog_Category

from product.models import Product_Category, Product, Product_version, Shopping_card, ItemInShoppingCart

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('')

class ProductVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_version
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    total_quantity = serializers.SerializerMethodField()
    main_version = serializers.SerializerMethodField()
    versions = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id','title', 'discount', 'price', 'designer', 'brand', 'mini_description', 'full_description', 'info', 'info_delivery', 'product_category', 'total_quantity', 'main_version', 'versions']

    def get_total_quantity(self,obj):
        return obj.total_quantity

    def get_main_version(self,obj):
        return ProductVersionSerializer(obj.main_version).data

    def get_versions(self,obj):
        qs = obj.versions.exclude(id=obj.main_version.id)
        return ProductVersionSerializer(qs, many=True).data



class Product_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Category
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
    
class Blog_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_Category
        fields = '__all__'


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    def exists(self):
        return User.objects.filter(email=self.initial_data['email']).exists()

    def get_user(self):
        return User.objects.get(email=self.initial_data['email'])


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

# class Product_category_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product_Category
#         fields = '__all__'

# class RegistrationSerializers(serializers.ModelSerializer):

#     password_confirmation = serializers.CharField(style={'input_type' : 'password'}, write_only=True)

#     class Meta:
#         model = get_user_model()
#         fields = ['first_name','last_name','email','phone','adress','second_adress','country','town','password','password_confirmation']
#         extra_kwargs = {
#             'password' : {'write_only' : True},
#         }

#     def create(self, validated_data):
#         user = get_user_model().objects.create_user(**validated_data)
#         return user

    # def save(self):
    #     user = User(
    #         first_name = self.validated_data['first_name'],
    #         last_name = self.validated_data['last_name'],
    #         email = self.validated_data['email'],
    #         phone = self.validated_data['phone'],
    #         adress = self.validated_data['adress'],
    #         second_adress = self.validated_data['second_adress'],
    #         country = self.validated_data['country'],
    #         town = self.validated_data['town'],
    #     )
    #     password = self.validated_data['password'],
    #     password_confirmation = self.validated_data['password_confirmation']

    #     if password != password_confirmation:
    #         raise serializers.ValidationError({'password' : 'Passwords must match.'})
    #     user.set_password(password)
    #     user.save()
    #     return user



UserModel = get_user_model()


class RegistrationSerializers(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(style={'input_type' : 'password'}, write_only=True)
    password = serializers.CharField(style={'input_type' : 'password'}, write_only=True)

    def validate(self, attrs):
        password=attrs['password']
        password_confirmation=attrs.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError({'password' : 'Passwords must match.'})
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['username'] = validated_data['email']
        user = super().create(validated_data=validated_data)
        user.set_password(password)
        user.save()
        return user
            
        

    class Meta:
        model = UserModel
        fields = ['first_name','last_name','email','phone','adress','second_adress','country','town','password','password_confirmation']
        extra_kwargs = {
            'password' : {'write_only' : True},
        }
    

class CardSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Shopping_card
        fields = '__all__'
    
class CardItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = ItemInShoppingCart
        fields = '__all__'


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'