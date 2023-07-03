from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('base_color/<int:pk>/', views.BaseDetail.as_view(), name="base_detail"),
    path('base_color/', views.BaseColorList.as_view(), name="base_color_list"),
    path('allColors/', views.AllColors.as_view(), name="all_colors"),
    path('allColors/new/', views.ColorCreate.as_view(), name="color_create"),
    path('allColors/update/<int:shade_pk>/', views.ColorUpdate.as_view(), name="color_update"),
    path('allColors/delete/<int:shade_pk>/', views.FromBaseShadeDelete.as_view(), name='shade_delete'),
]