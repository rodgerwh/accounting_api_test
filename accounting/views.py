from accounting.models import Transaction, UserCategory, Category, CustomUser
from accounting.serializers import (
    TransactionSerializer,
    UserCategorySerializer,
    CategorySerializer,
    CustomUserSerializer,
)
from django.http import HttpResponse
from rest_framework import viewsets
from accounting.tasks import send_statistics


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


def send_statistics_mail(request):
    send_statistics.delay()
    return HttpResponse("Emails sent")
