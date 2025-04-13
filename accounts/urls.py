from django.urls import path
from . import views

# ✅ This fixes the NoReverseMatch issue for namespaced URLs
app_name = 'accounts'

urlpatterns = [
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    # Profile
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change-password/', views.change_password, name='change_password'),
    
    # Orders and Wishlist
    path('orders/', views.order_history, name='order_history'),
    path('wishlist/', views.wishlist, name='wishlist'),
]
