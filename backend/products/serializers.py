from turtle import title
from wsgiref.validate import validator
from requests import request
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from . import validators
from api.serializers import UserPublicSerializer

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        )
    title = serializers.CharField(read_only= True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    edit_url = serializers.SerializerMethodField(read_only= True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        )
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            ]

    def get_my_user_data(self, obj):
        return {
            "username" : obj.user.username
        }


    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user

    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value

    # def create(self, validated_data):
    #     # email = validated_data.pop('email') 
    #     obj = super().create(validated_data)  
    #     # print(email, obj)
    #     return  obj
    # def create(self, validated_data):
    #     return Product.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title')
    #     email = validated_data.pop('email') 
    #     # return instance
    #     return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)