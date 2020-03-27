from django.urls import path
from . import views
app_name = "shop"

urlpatterns = [
    path('',views.index,name='index'),
    path('signin',views.signin,name="signin"),
    path('profile',views.profile,name="profile"),
    path('cart',views.cart,name="cart"),
    path('signup',views.signup,name="signup"),
]