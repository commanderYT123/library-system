# Generated by Django 5.0 on 2024-02-15 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_column="category",
                        max_length=50,
                        null=True,
                        verbose_name="category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_column="title",
                        max_length=50,
                        null=True,
                        verbose_name="title",
                    ),
                ),
                (
                    "author",
                    models.CharField(
                        db_column="author",
                        max_length=50,
                        null=True,
                        verbose_name="author",
                    ),
                ),
                (
                    "photo_book",
                    models.ImageField(
                        blank=True,
                        db_column="photo book",
                        null=True,
                        upload_to="photos",
                        verbose_name="photo book",
                    ),
                ),
                (
                    "photo_author",
                    models.ImageField(
                        blank=True,
                        db_column="photo author",
                        null=True,
                        upload_to="photos",
                        verbose_name="photo author",
                    ),
                ),
                (
                    "pages",
                    models.IntegerField(
                        blank=True, db_column="pages", null=True, verbose_name="pages"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        db_column="price",
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                        verbose_name="price",
                    ),
                ),
                (
                    "rentalPriceDay",
                    models.DecimalField(
                        db_column="rental price",
                        decimal_places=2,
                        max_digits=5,
                        null=True,
                        verbose_name="rental price",
                    ),
                ),
                (
                    "rental_period",
                    models.IntegerField(
                        blank=True,
                        db_column="rental period",
                        null=True,
                        verbose_name="rental period",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        db_column="active", default=True, verbose_name="active"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("avaible", "avaible"),
                            ("rental", "rental"),
                            ("sold", "sold"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="LMSapp.category",
                    ),
                ),
            ],
        ),
    ]
