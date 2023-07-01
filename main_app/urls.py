from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('base_color/<int:pk>/', views.BaseDetail.as_view(), name="base_detail"),
    path('base_color/', views.BaseColorList.as_view(), name="base_color_list")
]