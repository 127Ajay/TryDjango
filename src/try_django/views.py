from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    my_title = "hello there...."
    #string substituion in python
    #doc = "<h1>{title}</h1>".format(title=my_title)
    #Django_rendered_doc = "<h1>{{title}}</h1>".format(title=my_title)
    context = {"title":my_title,"MyList":[1,2,3,4,5]}
    return render(request, "home.html", context)

def about_page(request):
    return render(request, "about.html",{"title":"About Us Page"})

def contact_page(request):
    return render(request, "home.html",{"title":"Contact Us Page"})

def example_page(request):
    context         = {"title":"Example"}
    template_name   = "about.html"
    template_obj    = get_template(template_name)
    rendered_obj    = template_obj.render(context)
    return HttpResponse(rendered_obj)