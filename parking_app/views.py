from django.shortcuts import render, redirect
from .models import Slot
from .models import Slot, Booking
from django.contrib import messages
from django.db.models import DateField
from django.db.models.functions import TruncDate
from .models import Booking

def modify_slots(request):
    slots = Slot.objects.all()  # Fetch all slots from the database
    if request.method == "POST":
        slot_id = request.POST.get("slot_id")  # Get the slot ID from the form
        slot = Slot.objects.get(id=slot_id)  # Fetch the slot object
        slot.is_available = not slot.is_available  # Toggle the status
        slot.save()  # Save the updated slot
        return redirect("modify_slots")  # Redirect to the same page after updating
    return render(request, "parking_app/modify_slots.html", {"slots": slots})

def book_slot(request):
    slots = Slot.objects.filter(is_available=True)  # Fetch only available slots
    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        vehicle_number = request.POST.get("vehicle_number")
        vehicle_type = request.POST.get("vehicle_type")
        slot_id = request.POST.get("slot_id")
        slot = Slot.objects.get(id=slot_id)

        # Calculate amount based on vehicle type
        amount = 20 if vehicle_type == "Two-Wheeler" else 40

        # Create a new booking with payment status as "Completed"
        Booking.objects.create(
            customer_name=customer_name,
            vehicle_number=vehicle_number,
            vehicle_type=vehicle_type,
            amount=amount,
            slot=slot,
            payment_status="Completed",  # Mark payment as completed
        )

        # Mark the slot as occupied
        slot.is_available = False
        slot.save()

        # Add a success message
        messages.success(request, f"Slot {slot.slot_number} successfully booked for {customer_name} with payment of ₹{amount}!")

        # Re-render the same page with updated slots and success message
        slots = Slot.objects.filter(is_available=True)  # Refresh available slots
        return render(request, "parking_app/book_slot.html", {"slots": slots})

    return render(request, "parking_app/book_slot.html", {"slots": slots})

def view_bookings(request):
    # Group bookings by date
    bookings_by_date = (
        Booking.objects.annotate(date=TruncDate('booking_time'))
        .values('date')
        .order_by('-date')
        .distinct()
    )

    # Fetch all bookings for each date
    bookings = {}
    for entry in bookings_by_date:
        date = entry['date']
        bookings[date] = Booking.objects.filter(booking_time__date=date)

    return render(request, "parking_app/view_bookings.html", {"bookings": bookings})