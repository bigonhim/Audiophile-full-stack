from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    customer = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=200,null=True,blank=True)

    def __str__ (self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    price=models.FloatField(max_length=100,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    description = models.CharField(max_length=555,blank=True,null=True)
    number = models.CharField(max_length=255,null=True,blank=True)
 
    @property
    def ImageUrl(self):
        try:
             url = self.image.url
        except:
             url = ''
        return url

class Headphone(Product):

    def __str__ (self):
        return str(self.id)
    
class Speaker(Product):

    def __str__ (self):
        return str(self.id)
    
class Earphone(Product):

    def __str__ (self):
        return str(self.id)
    
class Order(models.Model):
    order_id = models.CharField(primary_key=True)
    customer= models.ForeignKey(Customer,related_name='orders',on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    
    def __str__ (self):
        return self.customer.name
    
    @property
    def orderItemsTotalPrice(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def totalVat(self):
        totalVat = 0.16 * self.orderItemsTotalPrice
        return totalVat
    @property
    def totalOrderPrice(self):
        total_price = 50 + self.totalVat + self.orderItemsTotalPrice
        return total_price

    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.product.name
    def product_price(self):
        return self.product.price
    def product_image(self):
        return self.product.ImageUrl
    def product_name(self):
        return self.product.name
    def product_pk(self):
        return str(self.product.pk)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
  
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete = models.SET_NULL,blank = True,null = True)
    name = models.CharField(max_length=200,null=True)
    email_address = models.EmailField(max_length=200,null=True)
    phone_number = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    zipcode= models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=100,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.email_address    






     

