from django.db import models
from django.utils.text import slugify

class DeliveryTime(models.IntegerChoices):
    ONE_TO_TWO_DAYS = 2, '1–2 days'
    THREE_TO_FIVE_DAYS = 5, '3–5 days'
    SEVEN_TO_TEN_DAYS = 10, '7–10 days'

    ONE_MONTH = 30, '1 month'
    TWO_MONTHS = 60, '2 months'
    THREE_MONTHS = 90, '3 months'


class ProductBrand(models.TextChoices):
    NIKE = 'nike', 'Nike'
    ADIDAS = 'adidas', 'Adidas'
    PUMA = 'puma', 'Puma'
    REEBOK = 'reebok', 'Reebok'
    UNIQLO = 'uniqlo', 'Uniqlo'
    

class ProductSize(models.TextChoices):
    XS = 'XS', 'XS'
    S = 'S', 'S'
    M = 'M', 'M'
    L = 'L', 'L'
    XL = 'XL', 'XL'
    XXL = 'XXL', 'XXL'

    SIZE_36 = '36', '36'
    SIZE_37 = '37', '37'
    SIZE_38 = '38', '38'
    SIZE_39 = '39', '39'
    SIZE_40 = '40', '40'
    SIZE_41 = '41', '41'
    SIZE_42 = '42', '42'

    FREE_SIZE = 'free', 'Free Size'


class ColorChoices(models.TextChoices):
    BLACK = "black", "Black"
    WHITE = "white", "White"
    RED = "red", "Red"
    BLUE = "blue", "Blue"
    GREEN = "green", "Green"
    YELLOW = "yellow", "Yellow"
    ORANGE = "orange", "Orange"
    PURPLE = "purple", "Purple"
    GRAY = "gray", "Gray"
    BROWN = "brown", "Brown"


class ProductCondition(models.TextChoices):
    NEW = 'new', 'New'
    USED = 'used', 'Used'
    REFURBISHED = 'refurbished', 'Refurbished'
    DAMAGED = 'damaged', 'Damaged'
    LIKE_NEW = 'like_new', 'Like New'


class Category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, unique = True)
    image = models.FileField(upload_to = 'images/category')
    desc = models.TextField()
    view = models.PositiveBigIntegerField(default=0)
    color = models.CharField(max_length = 50, choices = ColorChoices.choices, default = ColorChoices.BLACK)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):

        slug = slugify(self.name)
        number = 1

        while Category.objects.filter(slug = slug).exists():
            slug = slugify(self.name) + f"-{number}"
            number += 1

        self.slug = slug

        return super().save(*args, **kwargs)


class ProductCategory(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, unique = True)
    category = models.ForeignKey("Category", on_delete = models.CASCADE, related_name = "product_categories")
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):

        slug = slugify(self.name)
        number = 1

        while ProductCategory.objects.filter(slug = slug).exists():
            slug = slugify(self.name) + f"-{number}"
            number += 1

        self.slug = slug

        return super().save(*args, **kwargs)


class Country(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, unique = True)
    icon = models.FileField(upload_to = 'images/countries_icons')
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        slug = slugify(self.name)
        number = 1

        while Country.objects.filter(slug = slug).exists():
            slug = slugify(self.name) + f"-{number}"
            number += 1

        self.slug = slug

        return super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 150, unique = True)
    desc = models.TextField()
    main_image = models.FileField(upload_to = 'product/image')
    price = models.BigIntegerField()
    country = models.ForeignKey("Country", on_delete=models.SET_NULL, null=True, blank=True, related_name = "products")
    product_category = models.ForeignKey("ProductCategory", on_delete = models.SET_NULL, null=True, blank=True, related_name = "products")
    quantity = models.BigIntegerField(default = 0)
    view = models.BigIntegerField(default = 0)
    year = models.SmallIntegerField()
    delivery_time = models.IntegerField( choices=DeliveryTime.choices, default=DeliveryTime.ONE_TO_TWO_DAYS)
    star = models.BigIntegerField(default = 0)
    company = models.CharField(max_length = 150)
    brand = models.CharField(max_length = 100, choices=ProductBrand.choices, default=ProductBrand.NIKE)
    size = models.CharField(max_length = 50, choices=ProductSize.choices, default=ProductSize.XL)
    discount = models.SmallIntegerField(default = 0)  
    color = models.CharField(max_length = 100, choices=ColorChoices.choices, default=ColorChoices.BLACK)
    verified = models.BooleanField(default = False)
    recomended = models.BooleanField(default = False)
    condition = models.CharField(max_length = 150, choices=ProductCondition.choices, default=ProductCondition.NEW)
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):

        slug = slugify(self.name)
        number = 1

        while Product.objects.filter(slug = slug).exists():
            slug = slugify(self.name) + f"-{number}"
            number += 1

        self.slug = slug

        return super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = "product_images")
    image = models.FileField(upload_to = 'product_image/image')
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.product.name


class Service(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200, unique = True)
    image = models.FileField(upload_to = 'service/image')
    desc = models.TextField()
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):

        slug = slugify(self.title)
        number = 1

        while Service.objects.filter(slug = slug).exists():
            slug = slugify(self.title) + f"-{number}"
            number += 1

        self.slug = slug

        return super().save(*args, **kwargs)