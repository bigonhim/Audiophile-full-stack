from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .models import Customer,Headphone,Speaker,Earphone,OrderItem,Product,Order,ShippingAddress
from .serializers import *
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404
from django.views.generic import TemplateView




def home(request):
    return render(request,'index.html')
def cart(request):
    return render(request,'cart.html')
def thankyou(request):
    return render(request,'thankyou.html')

class Checkout(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        order_items = OrderItem.objects.all()
        orderitems_serializer = self.serializer_class(order_items, many=True)
        serializer3 = OrderSerializer( orders, many = True)
        context = {
            'orderItems': orderitems_serializer.data,
            'orders' : serializer3.data
        }

        return render(request, 'checkout.html', context)   
        
    
class Headphones(generics.ListAPIView):
    queryset1 = Headphone.objects.all()
    serializer_class1 = HeadphoneSerializer
    serializer_class2 = OrderItemSerializer
    

    def get(self, request, *args, **kwargs):
        headphones= self.queryset1
        orderItems = OrderItem.objects.all()
        for order_item in orderItems:
            if order_item.quantity == 0:
                order_item.delete()
        orders = Order.objects.all()
        headphone_serializer = self.serializer_class1(headphones, many=True)
        orderitems_serializer = self.serializer_class2(orderItems, many=True)
        serializer3 = OrderSerializer(orders,many = True)
        context = {
                  'headphones' :headphone_serializer.data,
                  'orderItems' :orderitems_serializer.data,
                  'orders' : serializer3.data
                   }
        return render(request,'headphones.html',context)
    
class Speakers(generics.ListCreateAPIView):
    queryset1 = Speaker.objects.all()
    serializer_class1 = SpeakerSerializer
    serializer_class2 = OrderItemSerializer
    

    def get(self, request, *args, **kwargs):
        speakers= self.queryset1
        orderItems = OrderItem.objects.all()
        for order_item in orderItems:
            if order_item.quantity == 0:
                order_item.delete()
        orders = Order.objects.all()
        speaker_serializer = self.serializer_class1(speakers, many=True)
        orderitems_serializer = self.serializer_class2(orderItems, many=True)
        serializer3 = OrderSerializer(orders,many = True)
        context = {
                  'speakers' :speaker_serializer.data,
                  'orderItems' :orderitems_serializer.data,
                  'orders':serializer3.data
                   }
        return render(request,'speakers.html',context)

class Earphones(generics.ListCreateAPIView):
    queryset1 = Earphone.objects.all()
    serializer_class1 = EarphoneSerializer
    serializer_class2 = OrderItemSerializer
    

    def get(self, request, *args, **kwargs):
        earphones= self.queryset1
        orders = Order.objects.all()
        orderItems = OrderItem.objects.all()
        for order_item in orderItems:
            if order_item.quantity == 0:
                order_item.delete()
        earphone_serializer = self.serializer_class1(earphones, many=True)
        orderitems_serializer = self.serializer_class2(orderItems, many=True)
        serializer3 = OrderSerializer(orders,many = True)
        context = {
                  'earphones' :earphone_serializer.data,
                  'orderItems' :orderitems_serializer.data,
                  'orders' : serializer3.data
                   }
        return render(request,'earphones.html',context)
    
class HeadphoneDetail(APIView):

    def get_object(self, pk):
        try:
            return Headphone.objects.get(pk=pk)
        except Headphone.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        headphone = self.get_object(pk)
        orders = Order.objects.all()
        orderitems = OrderItem.objects.all()
        for order_item in orderitems:
            if order_item.quantity == 0:
                order_item.delete()
        serializer = HeadphoneSerializer(headphone)
        serializer2 = OrderItemSerializer(orderitems,many=True)
        serializer3 = OrderSerializer(orders,many=True)
        context = {
            'product': serializer.data,
            'orderItems': serializer2.data,
            'orders' : serializer3.data
            }
        return render(request,'product.html',context)
    
class SpeakerDetail(APIView):

    def get_object(self, pk):
        try:
            return Speaker.objects.get(pk=pk)
        except Speaker.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        speaker= self.get_object(pk)
        orderitems = OrderItem.objects.all()
        for order_item in orderitems:
            if order_item.quantity == 0:
                order_item.delete()
        orders = Order.objects.all()
        serializer = SpeakerSerializer(speaker)
        serializer2 = OrderItemSerializer(orderitems,many=True)
        serializer3 = OrderSerializer(orders,many = True)
        context = { 
                  'product': serializer.data,
                  'orderItems': serializer2.data,
                  'orders' : serializer3.data
                  }
        return render(request,'product.html',context)
    
class EarphoneDetail(APIView):

    def get_object(self, pk):
        try:
            return Earphone.objects.get(pk=pk)
        except Earphone.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        earphone = self.get_object(pk)
        orderitems = OrderItem.objects.all()
        for orderitem in orderitems:
            if orderitem.quantity == 0:
                orderitem.delete()
        serializer = EarphoneSerializer(earphone)
        serializer2 = OrderItemSerializer(orderitems,many=True)
        context = {
                   'product': serializer.data,
                   'orderItems': serializer2.data 
                   }
        return render(request,'product.html',context)
     
class OrderItems(TemplateView,generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer2 = OrderSerializer(orders,many = True)
        order_items = self.get_queryset()
        for order_item in order_items:
            if order_item.quantity == 0:
                order_item.delete()
        serializer = self.get_serializer(order_items, many=True)

        # total_price = Order.orderItemsTotalPrice 
        context = {
            'orderItems': serializer.data,
            'orders': serializer2.data
        }
        return render(request,'index.html',context)


class AddCartItemNumber(APIView):
    def post(self, request, format=None):
        customer = get_object_or_404(Customer, pk=1)   
        product_id = request.data.get('product_id')
        # Get or create the order for the customer
        product = get_object_or_404(Product, pk=product_id)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        # Try to get an existing order item or create a new one if it doesn't exist
        quantity = request.data.get('quantity',1)  # Default to 1 if not provided
        order_item, created = OrderItem.objects.get_or_create(
            order=order,
            product=product,
            defaults={'quantity': quantity}
        )
        
        if not created:
            # If the order item already exists, update its quantity
            order_item.quantity = quantity
            order_item.save()
        
        # Serialize the updated order item
        serializer = OrderItemSerializer(order_item)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddToCart(APIView):
    def post(self,request,format=None):
        customer = get_object_or_404(Customer, pk=1) 
        product_id = request.data.get('product_id') 
        product = get_object_or_404(Product, pk=product_id) 
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        quantity = 1
        order_item, created = OrderItem.objects.get_or_create(
            order=order,
            product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            # If the order item already exists, update its quantity
            order_item.quantity = quantity
            order_item.save()
        serializer = OrderItemSerializer(order_item)   
  
        return Response(serializer.data, status=status.HTTP_200_OK)   

class CheckoutDetails(APIView):
    def post(self,request,format = None):
        customer = get_object_or_404(Customer, pk=1)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)


        name = request.data.get('name')
        email_address= request.data.get('emailAddress')
        phone_number= request.data.get('phoneNumber')
        address = request.data.get('address')
        city = request.data.get('city')
        zipcode = request.data.get('zipcode')
        country = request.data.get('country')

        if ShippingAddress.objects.filter(order=order).exists():
            return Response({"message": "Shipping information has already been submitted."}, status=status.HTTP_400_BAD_REQUEST)


        data = ShippingAddress.objects.create(
            customer = customer,
            order = order,
            name = name,
            email_address = email_address,
            phone_number = phone_number,
            address = address,
            city = city,
            zipcode = zipcode,
            country = country
        )

        serializer = ShippingAddressSerializer(data=data)

        if serializer.is_valid():
            serializer.save() 
            return Response({'message': 'Shipping address saved successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



   






