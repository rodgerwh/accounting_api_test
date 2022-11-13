from rest_framework import viewsets

from accounting.models import Transaction, UserCategory, Category, CustomUser
from accounting.serializers import (
    TransactionSerializer,
    UserCategorySerializer,
    CategorySerializer,
    CustomUserSerializer,
)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class UserCategoryViewSet(viewsets.ModelViewSet):
    queryset = UserCategory.objects.all()
    serializer_class = UserCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
