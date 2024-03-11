from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        null=True, max_length=50, verbose_name="category", db_column="category"
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    statusBook = [
        ("avaible", "avaible"),
        (
            "rental",
            "rental",
        ),
        ("sold", "sold"),
    ]
    title = models.CharField(
        null=True, max_length=50, verbose_name="title", db_column="title"
    )
    author = models.CharField(
        null=True, max_length=50, verbose_name="author", db_column="author"
    )
    photo_book = models.ImageField(
        null=True,
        blank=True,
        upload_to="photos",
        verbose_name="photo book",
        db_column="photo book",
    )
    photo_author = models.ImageField(
        null=True,
        blank=True,
        upload_to="photos",
        verbose_name="photo author",
        db_column="photo author",
    )
    pages = models.IntegerField(
        null=True, blank=True, verbose_name="pages", db_column="pages"
    )
    price = models.DecimalField(
        null=True,
        blank=True,
        verbose_name="price",
        db_column="price",
        max_digits=5,
        decimal_places=2,
    )
    rentalPriceDay = models.DecimalField(
        null=True,
        max_digits=5,
        decimal_places=2,
        verbose_name="rental price",
        db_column="rental price",
    )
    rental_period = models.IntegerField(
        null=True, blank=True, verbose_name="rental period", db_column="rental period"
    )
    total_rental = models.DecimalField(
        default=0,
        null=True,
        max_digits=5,
        decimal_places=2,
        verbose_name="total rental",
        db_column="total rental",
    )
    active = models.BooleanField(
        default=True, verbose_name="active", db_column="active"
    )
    status = models.CharField(max_length=50, choices=statusBook, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, null=True, blank=True
    )

    def __str__(self):
        return self.title
