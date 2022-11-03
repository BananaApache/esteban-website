
from django.urls import include, path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('', views.send_to_main),
    path('sub1/', views.sub1),
    path('sub2/', views.sub2),
    path('sub3/', views.sub3),
]
