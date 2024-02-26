from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
cats = {
    "food": "food",
    "animal-goods": "animal goods"
}

def index(request):
    # breakpoint()
    # print(request)
    return HttpResponse("<h2>Main page</h2>")

def categories(request):
    return HttpResponse("<h3>Catalog</h3>")

def category(request, cat):
    # if int(cat) > 2:
    #     return redirect('categories') # Пример использования перенаправления
    # if request.GET:
    #     print(request.GET) # для использования query-параметров
    return HttpResponse(f"<h3>Items from category {cats.get(str(cat))}</h3>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h3>Page not found</h3>")