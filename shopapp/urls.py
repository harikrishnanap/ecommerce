from . import views
from django.urls import path

app_name = 'shopapp'
urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('slug/<slug:c_slug>/', views.allProdCat, name='products_by_cat'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='proCatdetail'),

]
