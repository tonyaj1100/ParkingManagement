from django.db import models

class Slot(models.Model):
    slot_number = models.IntegerField(unique=True)  # Unique slot number
    is_available = models.BooleanField(default=True)  # True if the slot is free
    last_updated = models.DateTimeField(auto_now=True)  # Tracks when the status was last updated

    def __str__(self):
        return f"Slot {self.slot_number} - {'Available' if self.is_available else 'Occupied'}"