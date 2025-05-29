from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Calculator(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='calculators')
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CalculatorField(models.Model):
    calculator = models.ForeignKey(Calculator, on_delete=models.CASCADE, related_name='fields')
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=150)
    field_type = models.CharField(max_length=50, choices=[
        ('number', 'Number'),
        ('text', 'Text'),
        ('dropdown', 'Dropdown'),
    ], default='number')
    required = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.calculator.name} - {self.name}"