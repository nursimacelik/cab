from django.urls import path
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('hakkimizda/', views.about, name='about'),
    path('faaliyetalanlarimiz/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('iletisim/', views.contact, name='contact'),
    path('blog/<int:pk>/', views.post_detail, name='post_detail'),
    path('arama/', views.search, name='search_results'),
    path('basarili/', views.success, name='success'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)