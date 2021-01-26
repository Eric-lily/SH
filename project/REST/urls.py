from django.urls import path
from rest_framework.routers import DefaultRouter
from REST import views

router = DefaultRouter()

router.register('user',views.UserViewSet)
router.register('book',views.BookViewSet)