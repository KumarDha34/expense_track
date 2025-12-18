from django.urls import path
from . import views

urlpatterns = [
    path("",views.ExpenseAPIView.as_view(),name="expenses")
]
