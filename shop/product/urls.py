from django.urls import path
from .views import HomeView, product_detail, category_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<int:pk>', product_detail, name='detail'),
    path('category/<int:cat_id>', category_view, name='category'),

]