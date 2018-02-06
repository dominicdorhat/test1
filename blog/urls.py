# blog/urls.py 

from django.urls import path 

from . import views 

app_name = "blog"
urlpatterns = [
    path('', views.HomeListView.as_view(), name = 'home'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name = 'post_detail' ),
    path('post/create', views.BlogCreateView.as_view(), name = 'post_create'),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name = 'post_edit'),
]