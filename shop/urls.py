"""
URL configuration for KsiegarniaS18 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from shop import views

urlpatterns = [
    path('add_author/', views.AddAuthorView.as_view(), name="add_author"),
    path('add_book/', views.AddBookView.as_view(), name="add_book"),
    path('book_list/', views.BookListView.as_view(), name="book_list"),
    path('author_list/',views.AuthorListView.as_view(), name="author_list"),
    path('add_magazine/', views.AddMagazineView.as_view(), name="add_magazine"),
    path('add_publisher/', views.AddPublisherView.as_view(), name="add_publisher"),
    path('publisher_list/', views.PublisherListView.as_view(), name="list_publisher"),
    path('update_publisher/<int:pk>/', views.UpdatePublisherView.as_view(), name="update_publisher"),
    path('delete_publisher/<int:pk>/', views.DeletePublisherView.as_view(), name="delete_publisher"),
    path('add_book_to_cart/<int:book_pk>/', views.AddBookToCartView.as_view(), name="add_book_to_cart"),
    path('cart/', views.ShowCardView.as_view(), name="cart"),
    path('create_order/', views.CreateOrderView.as_view(), name="create_order"),
    path('order_list/', views.OrderListView.as_view(), name="order_list"),
    path('detail_odrer/<int:pk>/', views.DetailOrderView.as_view(), name="detail_order"),
    path('detail_book/<int:pk>/', views.DetailBookView.as_view(), name="detail_book"),
    path('add_comment/<int:book_pk>/', views.AddCommentView.as_view(), name="add_comment"),
    path('update_comment/<int:pk>/', views.UpdateCommentView.as_view(), name="update_comment"),
]
