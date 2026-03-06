from django.shortcuts import render, get_object_or_404, redirect

from .models import Blog, Category
from django.db.models import Q

# Create your views here.
def get_posts_by_category(request, category_id):
    # Fetch posts that belongs to specific category based on the category_id
    posts = Blog.objects.filter(status="Published", category=category_id)
    #use try/except block whenever object is not found and return something/ do some custom action
    try:

        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    
    # use get_object_or_404 when u want to show 404 page if the category does not exist
    # category = get_object_or_404(Category, pk=category_id)


    context ={
        'posts':posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status = "Published")
    # print(single_blog)

    context = {
        'single_blog': single_blog
    }
    return render(request, 'single_blog_page.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status="Published")

    context = {
        'blogs':blogs,
        'keyword':keyword,
    }

    return render(request, 'search.html', context)