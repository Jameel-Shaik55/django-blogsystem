from .models import Category
from aside.models import SocialLink
def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_socialLinks(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)
