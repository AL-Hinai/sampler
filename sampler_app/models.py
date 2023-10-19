from django.db import models

USER_TYPE_CHOICES = (
    ('staff', 'Staff'),
    ('student', 'Student'),
)

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

class HazardType(models.Model):
    name = models.CharField(max_length=50, choices=HAZARD_TYPE_CHOICES)

    def __str__(self):
        return self.name

class UserID(models.Model):
    id_value = models.CharField(max_length=10)

    def __str__(self):
        return self.id_value

class UserName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sample(models.Model):
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    user_name = models.ForeignKey(UserName, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserID, on_delete=models.CASCADE)
    sample_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    hazard_type = models.ManyToManyField(HazardType)
    submission_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()

    def __str__(self):
        return self.sample_name
