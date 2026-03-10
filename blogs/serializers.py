from rest_framework import serializers
from . models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "category",
            "author",
            "short_description",
            "blog_body",
            "status",
            "is_featured",
        ]