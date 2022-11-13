from accounting.views import (
    TransactionViewSet,
    CategoryViewSet,
    UserCategoryViewSet,
    CustomUserViewSet,
)
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register("transactions", TransactionViewSet)
router.register("categories", CategoryViewSet)
router.register("user-categories", UserCategoryViewSet)
router.register("user-list", CustomUserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("", include("rest_registration.api.urls")),
    path("auth-token/", obtain_auth_token),
]
