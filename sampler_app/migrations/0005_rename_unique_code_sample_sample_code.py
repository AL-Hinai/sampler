# Generated by Django 4.2.3 on 2023-10-18 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sampler_app', '0004_alter_sample_unique_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='unique_code',
            new_name='sample_code',
        ),
    ]