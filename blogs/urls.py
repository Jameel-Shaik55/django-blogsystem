from django.urls import path, include
from . import views
from .serializers import BlogSerializer
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet),

urlpatterns = [
    path('<int:category_id>/', views.get_posts_by_category, name="get_posts_by_category"),
    path('', include(router.urls)),

]