from accounting.models import Transaction, UserCategory, Category, CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = (
            "username",
            "balance",
        )
        read_only_fields = (
            "username",
            "balance",
        )
        model = CustomUser


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = (
            "id",
            "user",
            "category",
            "organization",
            "sum",
            "description",
            "created",
        )
        model = Transaction


class UserCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = (
            "user",
            "category",
        )
        model = UserCategory


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ("category",)
        model = Category
