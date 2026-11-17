from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import send_mail
import json



def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST, request.FILES)  # request.FILES for photo
        if form.is_valid():
            form.save()
            messages.success(request, "Your appointment has been booked successfully!")
            return redirect(request.path)  # define this URL
    else:
        form = AppointmentForm()
    return render(request, "book_appointment.html", {"form": form})



def cloudwatch_alert(request):
    if request.method == "POST":
        data = json.loads(request.body)
        # Example: log the alarm message
        print("CloudWatch Alarm:", data)

        send_mail(
            'cloudwatch_alert',  #subject
            'Your S3 bucket size limit is almost full.',    #message
            "alerts@clinic.com",      # From
            ["20031955@students.koi.edu.au"],     # To
            fail_silently=False,
        )

        return JsonResponse({"status": "ok"})
    return JsonResponse({"error": "Invalid request"}, status=400)