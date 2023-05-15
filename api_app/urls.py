from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_home_page, name="product-home-page"),
    path('<int:pk>/', views.product_detail_page, name="product-detail-page"),
]