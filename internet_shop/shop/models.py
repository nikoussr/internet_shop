from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    """Модель категории товаров"""
    name = models.CharField("Название категории", max_length=256)
    description = models.TextField("Описание категории", blank=True, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель товара"""
    name = models.CharField("Название товара", max_length=256)
    description = models.TextField("Описание товара", blank=True, null=True)
    price = models.DecimalField(
        "Цена",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    stock_quantity = models.PositiveIntegerField("Количество на складе", default=0)
    image_url = models.URLField("Ссылка на изображение", blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="products"
    )
    discount = models.DecimalField(
        "Скидка (%)",
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    is_available = models.BooleanField("Доступен для заказа", default=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        ordering = ["-created_at", "name"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Customer(models.Model):
    """Модель покупателя"""
    username = models.CharField("Имя пользователя", max_length=150, unique=True)
    email = models.EmailField("Электронная почта", unique=True)
    first_name = models.CharField("Имя", max_length=256)
    last_name = models.CharField("Фамилия", max_length=256)
    phone_number = models.CharField("Номер телефона", max_length=20, blank=True, null=True)
    address = models.TextField("Адрес", blank=True, null=True)
    loyalty_points = models.PositiveIntegerField("Бонусные баллы", default=0)
    is_active = models.BooleanField("Активен", default=True)
    date_joined = models.DateTimeField("Дата регистрации", auto_now_add=True)
    last_login = models.DateTimeField("Последний вход", blank=True, null=True)

    class Meta:
        ordering = ["-date_joined"]
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
