from django.db import models



class Appointment(models.Model):

    REASONS = [
        ("Consult with GP", "Consult with GP"),
        ("Vaccination", "Vaccination"),
        ("Pathology Test", "Pathology Test"),
        ("Radiology", "Radiology"),
        ("Other", "Other"),
    ]

    DOCTORS = [
        ("Hari Prasad Koirala", "Hari Prasad Koirala"),
        ("Deep Kumar Paudel", "Deep Kumar Paudel"),
        ("Jennifer Lee", "Jennifer Lee"),
        ("Michael Douglas", "Michael Douglas"),
        ("Aanand Bhatt", "Aanand Bhatt"),
    ]


    patient_name = models.CharField(max_length=50)
    patient_photo = models.ImageField(upload_to='patient_photos/')
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    appointment_date = models.DateTimeField()
    doctor = models.CharField(max_length=50, choices=DOCTORS)
    reason = models.CharField(max_length=30, choices=REASONS)



    def __str__(self):
        return f"{self.patient_name} - {self.appointment_date}"
