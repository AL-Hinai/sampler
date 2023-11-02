from django.db import models
import random
import string

def generate_unique_code():
    letters = string.ascii_letters
    numbers = ''.join(random.choice(string.digits) for _ in range(4))
    letter = random.choice(letters)
    return f"{numbers}{letter}"

class HazardType(models.Model):
    HAZARD_TYPE_CHOICES = (
        ('chemical_hazards', 'Chemical Hazards'),
        ('biological_hazards', 'Biological Hazards'),
        ('radiological_hazards', 'Radiological Hazards'),
        ('physical_hazards', 'Physical Hazards'),
        ('fire_and_explosion_hazards', 'Fire and Explosion Hazards'),
        ('ergonomic_hazards', 'Ergonomic Hazards'),
        ('noise_hazards', 'Noise Hazards'),
        ('environmental_hazards', 'Environmental Hazards'),
        ('biological_safety_level', 'Biological Safety Level'),
        ('physical_security_hazards', 'Physical Security Hazards'),
    )

    name = models.CharField(max_length=50,choices=HAZARD_TYPE_CHOICES, unique=True)

    def __str__(self):
        return self.name

class Sample(models.Model):
    USER_TYPE_CHOICES = (
        ('staff', 'Staff'),
        ('student', 'Student'),
    )

    

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    user_name = models.CharField(max_length=10)
    user_id = models.CharField(max_length=10)
    sample_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    hazard = models.ManyToManyField(HazardType, blank=True)
    submission_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()
    unique_code = models.CharField(max_length=5, default=generate_unique_code, editable=False, unique=True)

    def __str__(self):
        return self.sample_name
