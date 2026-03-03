from django.urls import path
from . import views

urlpatterns = [
    path('<int:category_id>/', views.get_posts_by_category, name="get_posts_by_category")
]