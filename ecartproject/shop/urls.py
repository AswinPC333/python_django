from . import views
from django.urls import include, path

app_name='shop'
urlpatterns = [
    path('',views.AllProdCat,name='AllProdCat'),
    path('<slug:c_slug>/',views.AllProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name='prodCatDetail'),
]
