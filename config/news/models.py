from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, verbose_name="Category")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_add=True)

    def __str__(self) -> str:
        return f"{self.name}"
