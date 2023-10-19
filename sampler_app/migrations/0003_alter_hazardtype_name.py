# Generated by Django 4.2.3 on 2023-10-18 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampler_app', '0002_hazardtype_userid_username_remove_sample_hazard_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hazardtype',
            name='name',
            field=models.CharField(choices=[('chemical_hazards', 'Chemical Hazards'), ('biological_hazards', 'Biological Hazards'), ('radiological_hazards', 'Radiological Hazards'), ('physical_hazards', 'Physical Hazards'), ('fire_and_explosion_hazards', 'Fire and Explosion Hazards'), ('ergonomic_hazards', 'Ergonomic Hazards'), ('noise_hazards', 'Noise Hazards'), ('environmental_hazards', 'Environmental Hazards'), ('biological_safety_level', 'Biological Safety Level'), ('physical_security_hazards', 'Physical Security Hazards')], max_length=50),
        ),
    ]
