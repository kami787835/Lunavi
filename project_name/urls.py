"""
URL configuration for project_name project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from app_name.views import ProductListCreateView, ProductDetailAPIView,ProductListView,OrderListCreateAPIView
from .yasg import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('your-Product', ProductListCreateView.as_view(), name='your-models-list-create'),
    path('your-Product/<int:pk>/', ProductDetailAPIView.as_view(), name='your-model-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

