from django.contrib import admin
from django.urls import path
from products import views
from .views import index
from django.urls import path,include , re_path
from django.conf.urls.static import static , serve
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('api/products/', views.GetAllProducts.as_view()),
]
