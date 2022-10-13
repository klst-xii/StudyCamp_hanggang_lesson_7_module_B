from django.urls import path, re_path
from products.views import ProductListView, ProductDetailSlugView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    re_path(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detailed'),
]
