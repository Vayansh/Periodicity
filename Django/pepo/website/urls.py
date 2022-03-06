from django.urls import path 
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('period_tracker',views.period_tracker,name='period_tracker'),
    path('products',views.products,name='products'),
    path('blog',views.blog,name='blog'),
]
