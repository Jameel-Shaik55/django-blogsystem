from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category, Blog
from aside.models import About

def home(request):
    # THis return all the categories from the category table
    # categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status = "Published").order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status = "Published")

    try:
        about = About.objects.get()
    except:
        about = None
    # print(categories.query)
    # print(featured_posts)
    context = {
        # 'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
        'about':about,
    }
    return render(request, 'home.html', context)