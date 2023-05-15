from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    description = models.TextField()
    CATEGORIES_CHOICES = (
        ("Furniture", "Furniture"),
        ("Electronics", "Electronics"),
        ("Accessories", "Accessories"),
        ("Womenswear", "Womenswear"),
        ("Vehicles", "Vehicles"),
        ("Sporting goods", "Sporting goods"),
    )
    category = models.CharField(max_length=20, choices=CATEGORIES_CHOICES)
    image = models.ImageField(upload_to="product_images")
    
    def __str__(self):
        return self.title