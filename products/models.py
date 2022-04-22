from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

# Create your models here.
class Category(TimeStampedModel):
   name = models.CharField(max_length=255, unique=True) 
   slug = AutoSlugField(unique=True, populate_from='name', always_update=False)

   def __str__(self):
       return self.name


class Product(TimeStampedModel):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, populate_from='name', always_update=False)
    image = models.FileField(upload_to='products/%Y/%m/%d', blank=False, default='no_image.jpg')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


