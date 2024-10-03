from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(max_length=999, unique=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', verbose_name='Изображение', blank=True)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=7, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=7, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name + f'Количество - {self.quantity}'

    def display_id(self):
        return f'{self.id:05}'

    def sell_price(self):
        if self.discount:
           return round(self.price - self.price * self.discount / 100, 2)
        return self.price

