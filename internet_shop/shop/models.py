from collections import defaultdict

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
        ordering = ["created_at", "name"]
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

class Order(models.Model):
    """Модель заказа"""
    customer = models.CharField("Логин пользователя", max_length=50)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)
    is_paid = models.BooleanField("Оплачен", default=False)
    is_delivered = models.BooleanField("Доставлен", default=False)
    total_amount = models.DecimalField(
        "Сумма заказа",
        max_digits=10,
        decimal_places=2,
        default=0
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ #{self.id} от {self.customer}"


class OrderItem(models.Model):
    """Модель позиции в заказе"""
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="Заказ"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name="Товар"
    )
    quantity = models.PositiveIntegerField("Количество", validators=[MinValueValidator(1)])
    price_at_order = models.DecimalField(
        "Цена на момент заказа",
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = "Позиции заказа"

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def get_total_price(self):
        return self.quantity * self.price_at_order
