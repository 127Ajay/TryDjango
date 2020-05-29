from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<h1>This is Home page</h1>")

def about_page(request):
    return HttpResponse("<h1>This is About page</h1>")

def contact_page(request):
    return HttpResponse("<h1>This is Contact us page</h1>")