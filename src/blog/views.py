from django.shortcuts import render , get_object_or_404
from django.http import Http404
# Create your views here.
from .models import BlogPost

# def blog_post_detail_page(requests, id):
#     try:
#         obj = BlogPost.objects.get(id=id)
#     except BlogPost.DoesNotExist:
#         raise Http404
#     except ValueError:
#         raise Http404
#     template_name = 'blog_post_detail.html'
#     context = {"object": obj}
#     return render(requests, template_name, context)

def blog_post_detail_page(requests, slug):
   # obj = get_object_or_404(BlogPost, slug=slug)
    querySet = BlogPost.objects.filter(slug=slug)
    if querySet.count() == 0:
        raise Http404
    obj = querySet.first()
    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(requests, template_name, context)