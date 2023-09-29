from django.urls import path, include
from ExamProject.products import views

urlpatterns = (
    path('', views.products_page, name='products'),
    path('filter/<str:category_name>/', views.products_page, name='products_by_category'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>', views.remove_from_cart, name="remove_from_cart"),
    path('cart/', views.view_cart, name='view cart'),
    path('cart/<str:sort_type>/', views.view_cart, name='view cart sorted'),
    path('rate/<int:product_id>/<int:rating>/', views.rate, name='rate'),
    path('details/<int:pk>/', views.product_details_page, name='product details'),
    path('add-product/', views.add_product, name='add product'),
    path('edit-product/<int:pk>/', views.edit_product, name='edit product'),
    path('delete-product/<int:pk>/', views.delete_product, name='delete product'),
    path('review-product/<int:product_id>/', views.create_review, name='review product'),
    path('delete-review/<int:review_id>/', views.delete_review, name='delete review'),
)
