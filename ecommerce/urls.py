"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecommerce import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.OrderItems.as_view(),name='home'),
    path('checkout/',views.Checkout.as_view(),name='checkout'),
    path('thankyou/',views.thankyou,name='thankyou'),
    path('headphones/',views.Headphones.as_view(),name='headphones'),
    path('speakers/',views.Speakers.as_view(),name='speakers'),
    path('earphones/',views.Earphones.as_view(),name='earphones'),
    path('headphone/<int:pk>/',views.HeadphoneDetail.as_view(),name='headphone_detail'),
    path('speaker/<int:pk>/',views.SpeakerDetail.as_view(),name='speaker_detail'),
    path('earphone/<int:pk>/',views.EarphoneDetail.as_view(),name='earphone_detail'),
    path('cartquantity/',views.AddCartItemNumber.as_view(),name='cartquantity'),
    path('post/',views.AddToCart.as_view(),name='post'),
    path('checkoutinfo/',views.CheckoutDetails.as_view(),name='checkoutinfo')
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

