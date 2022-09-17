from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import loginUserViewSet, registerUserViewSet, editProfileViewSet, getAllUsers

router = DefaultRouter()
router.register(r'login', loginUserViewSet, basename='login')
router.register(r'register', registerUserViewSet, basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('users/', getAllUsers.as_view(), name='allUsers'),
    path('users/edit/', editProfileViewSet.as_view(), name='editProfile'),
]