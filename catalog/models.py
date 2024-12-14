from datetime import datetime
from django.db import models
from decimal import Decimal

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    """Создаем модель для продуктов."""

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование товара",
        help_text="Введите наименование товара",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание товара", **NULLABLE
    )
    image = models.ImageField(
        upload_to="products/photo",
        verbose_name="Изображение (превью)",
        help_text="Загрузите изображение товара",
        **NULLABLE,
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Выберите категорию товара",
        **NULLABLE,
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за покупку",
        help_text="Введите цену покупки (в рублях)",
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата создания (записи в БД)",
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
        help_text="Дата последнего изменения (записи в БД)",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ("name", "price")


class Category(models.Model):
    """Создаем модель для категорий."""

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание категории", **NULLABLE
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
