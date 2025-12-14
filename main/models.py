from django.db import models
from django.utils.text import slugify

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

class Category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, unique = True)
    image = models.ImageField(upload_to = 'category/image')
    desc = models.TextField()
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
    icon = models.ImageField(upload_to = 'country/image')
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
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 150, unique = True)
    desc = models.TextField()
    main_image = models.ImageField(upload_to = 'product/image')
    price = models.BigIntegerField()
    country = models.ForeignKey("Country", on_delete=models.SET_NULL, related_name = "products")
    product_category = models.ForeignKey("ProductCategory", on_delete = models.SET_NULL, related_name = "products")
    quantity = models.BigIntegerField(default = 0)
    review = models.BigIntegerField(default = 0)
    year = models.SmallIntegerField()
    delivery_time = models.CharField(max_length = 150)
    star = models.BigIntegerField(default = 0)
    company = models.CharField(max_length = 150)
    brand = models.CharField(max_length = 100)
    size = models.CharField(max_length = 50)
    dicount = models.SmallIntegerField(default = 0)  
    color = models.CharField(max_length = 100)
    verified = models.BooleanField(default = False)
    recomended = models.BooleanField(default = False)
    condition = models.CharField(max_length = 150)
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
    
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
    image = models.ImageField(upload_to = 'product_image/image')
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.product.title


class Service(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'service/image')
    desc = models.TextField()
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.title
