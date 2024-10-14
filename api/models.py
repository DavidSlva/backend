from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Categorias'

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Productos'