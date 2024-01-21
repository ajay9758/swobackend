from django.contrib import admin
from django.urls import path
from products import views
from .views import index
from django.urls import path,include , re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    # path("", index, name="index"),
    path('admin/', admin.site.urls),
    path('api/products/', views.GetAllProducts.as_view()),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}), 
    re_path(r'^.*$', TemplateView.as_view(template_name='base.html')), 
]
