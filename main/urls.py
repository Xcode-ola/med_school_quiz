from django.urls import path
from .views import index, update

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('update/<int:pk>/', update.as_view(), name="update")
]