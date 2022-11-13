from django.db import models
from django.contrib.auth.models import AbstractUser


DEFAULT_CATEGORIES = (
    "Care",
    "Wage",
    "Health",
    "Restaurants",
    "Car",
    "Education",
    "Recreation",
    "Payments",
    "Purchases",
    "Food",
    "Fare",
)


class CustomUser(AbstractUser):
    balance = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            for category in Category.objects.filter(category__in=DEFAULT_CATEGORIES):
                new_category = UserCategory(
                    category=category,
                    user=self,
                )
                new_category.save()
        else:
            super().save(*args, **kwargs)


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


class UserCategory(models.Model):
    class Meta:
        verbose_name_plural = "user categories"

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category}"


class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sum = models.FloatField(default=0)
    category = models.ForeignKey(UserCategory, on_delete=models.CASCADE)
    organization = models.CharField(max_length=30, default="not specified")
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sum} in category: {self.category}"

    def save(self, *args, **kwargs):
        self.user.balance += self.sum
        self.user.save()
        super().save(*args, **kwargs)
