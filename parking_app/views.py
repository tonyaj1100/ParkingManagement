from django.shortcuts import render, redirect
from .models import Slot

def modify_slots(request):
    slots = Slot.objects.all()  # Fetch all slots from the database
    if request.method == "POST":
        slot_id = request.POST.get("slot_id")  # Get the slot ID from the form
        slot = Slot.objects.get(id=slot_id)  # Fetch the slot object
        slot.is_available = not slot.is_available  # Toggle the status
        slot.save()  # Save the updated slot
        return redirect("modify_slots")  # Redirect to the same page after updating
    return render(request, "parking_app/modify_slots.html", {"slots": slots})