from django.urls import path
from . import views

urlpatterns = [
    path("modify-slots/", views.modify_slots, name="modify_slots"),
    path("book-slot/", views.book_slot, name="book_slot"),  # URL for slot modification page
]