from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GH_UserViewSet, LoginEndpoint

router = DefaultRouter()
router.register(r'gh_users', GH_UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginEndpoint.as_view()),  # Custom APIView
]
