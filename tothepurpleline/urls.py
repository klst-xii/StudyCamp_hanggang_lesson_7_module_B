from django.contrib import admin
from django.urls import path, include
from django.urls import re_path

from .views import home_page, contact_page
from accounts.views import RegisterView, login_page
from django.contrib.auth import views as auth_views
from products.views import ProductListView
from products.views import ProductDetailView
from products.views import ProductFeaturedListView
from products.views import ProductFeaturedDetailView
from products.views import ProductDetailSlugView
from socials.views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home_page, name='home'),
    path('contact/', contact_page, name='contact'),
    path('register/', RegisterView.as_view(), name='register'),
    path('featured/', ProductFeaturedListView.as_view(), name='featured_list' ),
    # path('featured/<int:pk>', ProductFeaturedDetailView.as_view(), name='featured_detailed'),
    re_path(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    path('logout/', auth_views.LogoutView.as_view(template_name="auth/logout.html"), name='logout'),
    path('login', login_page, name='login'),
    path('admin/', admin.site.urls),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='detailed'),
    path('socials/', PostListView.as_view(), name='post-list'),
    path('socials/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('socials/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('socials/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('socials/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('search/', include("search.urls", namespace='search')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)