from django.urls import path
from authentication.views import MyObtainTokenPairView, RegisterView, UserListView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('user/list/', UserListView.as_view(), name='user-list'),
]
