from django.shortcuts import render

# Create your views here.
from .models import BlogPost

def blog_post_detail_page(requests):
    obj = BlogPost.objects.get(id=2)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(requests, template_name, context)