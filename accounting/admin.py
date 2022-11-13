from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounting.forms import CustomUserCreationForm, CustomUserChangeForm
from accounting.models import CustomUser, Transaction, Category, UserCategory


class TransactionInLine(admin.StackedInline):
    model = Transaction
    extra = 0
    show_change_link = True


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "email",
        "username",
        "balance",
        "is_staff",
    )
    inlines = (TransactionInLine,)


class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "category",
        "sum",
        "organization",
        "description",
        "created",
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)


class UserCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "category",
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserCategory, UserCategoryAdmin)
