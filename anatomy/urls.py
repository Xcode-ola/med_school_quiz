from django.urls import path
from .views import index, summary, summary_overview_list, summary_overview_detail

urlpatterns = [
    path('', index.as_view(), name="ana_index"),
    path('<int:pk>/', summary.as_view(), name="summary"),
    path('overview/', summary_overview_list.as_view(), name="summary_overview"),
    path('overview/<int:pk>/', summary_overview_detail.as_view(), name="summary_overview_detail"),
]