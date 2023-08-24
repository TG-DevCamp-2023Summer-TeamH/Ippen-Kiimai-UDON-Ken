from django.urls import path
from . import views

app_name = "line_bot"

urlpatterns = [
    path('', views.index),
    path('stamp/<slug:user_id>', views.stamp, name="stampdata")
]
