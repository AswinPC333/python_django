from . import views
from django.urls import include, path

app_name='search_app'
urlpatterns = [
    path('',views.SearchResult,name='SearchResult'),
]