from django.urls import path
from . import views
app_name = "shop"

urlpatterns = [
    path('',views.index,name='index'),
    path('signin',views.signin,name="signin"),
    path('profile',views.profile,name="profile"),
    path('cart',views.cart,name="cart"),
    path('signup',views.signup,name="signup"),
    path('logout',views.logout,name="logout"),
    path("profile_update/<int:user_id>",views.profile_update,name="profile_update"),
    
]