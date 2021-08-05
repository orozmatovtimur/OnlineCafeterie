from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

# from account.views import logout_request
from main import views
from main.views import *

urlpatterns = [
    path('home/', MainPageView.as_view(), name='home'),
    path('<str:slug>/', DishListView.as_view(), name='list'),
    path('dish/<int:id>/', DishDetailView.as_view(), name='detail'),
    path('dish/<int:id>/comment', ReviewAdd.as_view(), name='add_comment_url'),
    path("login/", LoginView.as_view(), name="login"),
    path('dish/create/', DishCreateView.as_view(), name='create_dish'),
    path('dish/update/<int:id>/', DishUpdateView.as_view(), name='update_dish'),
    path('dish/delete/<int:id>/', DishDeleteView.as_view(), name='delete_dish'),

    # cart urls
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),

]

