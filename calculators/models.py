from django.db import models
from django.db import models
from django.utils.text import slugify



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True




class Category(BaseModel):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField(blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Calculator(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='calculators')
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    template = models.CharField(max_length=150)
    icon = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class CalculatorField(BaseModel):
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