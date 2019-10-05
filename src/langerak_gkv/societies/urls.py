from django.urls import path

from .views import SocietyDetailView

app_name = "societies"

urlpatterns = [
    path('<int:pk>/', SocietyDetailView.as_view(), name='detail'),
]
