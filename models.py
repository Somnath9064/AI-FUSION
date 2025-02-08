from django.db import models

class WasteManagement(models.Model):
    waste_type = models.CharField(max_length=100)  # Type of waste (e.g., plastic, organic)
    amount = models.FloatField()  # Amount of waste in kilograms
    disposal_method = models.CharField(max_length=100)  # How it is disposed (e.g., recycle, landfill)
    date_recorded = models.DateTimeField(auto_now_add=True)  # Automatically sets the current date

    def __str__(self):
        return f"{self.waste_type} - {self.amount} kg"

class PollutionControl(models.Model):
    pollution_type = models.CharField(max_length=100)  # Type of pollution (e.g., air, water)
    level = models.FloatField()  # Pollution level in PPM
    location = models.CharField(max_length=200)  # Location where it was recorded
    date_recorded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pollution_type} - {self.level} PPM"

class EnergyConsumption(models.Model):
    source = models.CharField(max_length=100)  # Source of energy (e.g., solar, coal)
    amount = models.FloatField()  # Energy consumed in kWh
    efficiency_rating = models.CharField(max_length=50)  # Efficiency rating (e.g., A+, B)
    date_recorded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source} - {self.amount} kWh"
