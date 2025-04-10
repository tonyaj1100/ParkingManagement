from django.urls import path
from . import views

urlpatterns = [
    path("modify-slots/", views.modify_slots, name="modify_slots"),  # URL for slot modification page
]