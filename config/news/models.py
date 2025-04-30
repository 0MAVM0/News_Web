from django.contrib.auth.models import User
from django.db import models

class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=self.model.Status.Published)

class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, unique=True, verbose_name="Category's Name")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"{self.name}"

class News(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Title Of The News")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="news/", null=True, blank=True)
    body = models.TextField()
    slug = models.SlugField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "News"
        verbose_name_plural = "News"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.user} - {self.news}"

    class Meta:
        ordering = ["-created_at"]

class Contact(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Name")
    email = models.EmailField(max_length=255, null=False, blank=False, verbose_name="Email")
    subject = models.CharField(max_length=255, null=False, blank=False, verbose_name="Subject")
    message = models.TextField(null=False, blank=False, verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"
