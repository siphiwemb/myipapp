from django.urls import path
from .views import MyIPView

urlpatterns = [
    path('myip/', MyIPView.as_view())
]
