from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='Categoria', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

# Create your models here.
class Product(models.Model):
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Seleciione la categoria del producto')
    name = models.CharField(verbose_name='Producto', max_length=100, unique=True)
    description = models.TextField(verbose_name='Descripcion del producto', max_length=600)
    price = models.DecimalField(verbose_name='Precio', max_digits=8, decimal_places=2, default=0.00)
    foto = models.ImageField(verbose_name='Agregar imagen', null=True, upload_to='imgProducts')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
