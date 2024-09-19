from rest_framework import serializers
from .models import Customer,Headphone,Speaker,Earphone,OrderItem,Order,ShippingAddress

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields =['name','email']


class HeadphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headphone
        fields = ['name','price','description','ImageUrl','number','pk']
class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = ['name','price','description','ImageUrl','number','pk']
class EarphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earphone
        fields = ['name','price','description','ImageUrl','number','pk']  
class OrderItemSerializer(serializers.ModelSerializer):
    product_price = serializers.SerializerMethodField()
    product_image = serializers.SerializerMethodField()
    product_name = serializers.SerializerMethodField()
    product_pk = serializers.SerializerMethodField()

    
    class Meta:
        model = OrderItem
        fields = ['order','quantity','product','product_price','product_image','product_name','pk','product_pk']  

    def get_product_price(self,obj):
        return obj.product_price()
    def get_product_image(self,obj):
        return obj.product_image()
    def get_product_name(self,obj):
        return obj.product_name()
    def get_product_pk(self,obj):
        return obj.product_pk()

class OrderSerializer(serializers.ModelSerializer):
    orderItemsTotalPrice = serializers.SerializerMethodField()
    totalVat = serializers.SerializerMethodField()
    totalOrderPrice = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['order_id','customer','complete','orderItemsTotalPrice','totalVat','totalOrderPrice']   

    def get_orderItemsTotalPrice(self,obj):
        return obj.orderItemsTotalPrice  
    def get_totalVat(self,obj):
        return obj.totalVat
    def get_totalOrderPrice(self,obj):
        return obj.totalOrderPrice     



class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ['customer','order','name','email_address','phone_number','address','zipcode','city','country']


def create(self, validated_data):
    """
    Create and return a new `Snippet` instance, given the validated data.
    """
    return OrderItem.objects.create(**validated_data)


                      
        
