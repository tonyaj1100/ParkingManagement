from django.db import models
from django.utils.timezone import now

class Slot(models.Model):
    slot_number = models.IntegerField(unique=True)  # Unique slot number
    is_available = models.BooleanField(default=True)  # True if the slot is free
    last_updated = models.DateTimeField(auto_now=True)  # Tracks when the status was last updated

    def __str__(self):
        return f"Slot {self.slot_number} - {'Available' if self.is_available else 'Occupied'}"
    
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)  # Auto-generated unique ID
    customer_name = models.CharField(max_length=100)  # Customer's name
    vehicle_number = models.CharField(max_length=20)  # Vehicle registration number
    VEHICLE_TYPE_CHOICES = [
        ('Two-Wheeler', 'Two-Wheeler'),
        ('Four-Wheeler', 'Four-Wheeler'),
    ]
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)  # Vehicle type
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Booking amount
    slot = models.ForeignKey('Slot', on_delete=models.CASCADE)  # Link to Slot model
    booking_time = models.DateTimeField(default=now)  # Booking timestamp
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='Pending')  # Payment status

    def __str__(self):
        return f"Booking {self.booking_id} - {self.customer_name}"