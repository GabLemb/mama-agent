from django.urls import path
from . import views

urlpatterns = [
    path("send/", views.chat_message, name="chat_message"),
]
