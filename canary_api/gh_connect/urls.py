from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GH_UserViewSet, LoginEndpoint, GitHubCallback, SaveRepository, GetSelectedRepository, WebhookEndpoint

router = DefaultRouter()
router.register(r'gh_users', GH_UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginEndpoint.as_view(), name="login"),  # Custom APIView
    path('callback/', GitHubCallback.as_view(), name="callback"),  # Custom APIView
    path('save-repository/', SaveRepository.as_view(), name="save_repository"),
    path('get-selected-repository/', GetSelectedRepository.as_view(), name='get_selected_repository'),
    path('webhook/', WebhookEndpoint.as_view(), name="webhook")
]
