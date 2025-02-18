from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.ProductDetailAPIView.as_view()),
    path("<int:pk>/update/", views.ProductUpdateAPIView.as_view()),
    path("<int:pk>/destroy/", views.ProductDestroyAPIView.as_view()),
    path("", views.ProductListCreateAPIView.as_view()),
]
