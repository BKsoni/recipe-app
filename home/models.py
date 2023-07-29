from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # email = models.EmailField()
    # phone = models.CharField(max_length=10)
    # image = models.ImageField()
    address = models.TextField(null=True, blank=True)
    # file = models.FileField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self) -> str:
        return self.name