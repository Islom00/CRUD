from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import BookModel


def index(request, ):
    q = request.GET.get("q")
    if q:
        data = BookModel.objects.filter(Q(title__icontains=q) | Q(summary__icontains=q))
    else:
        data = BookModel.objects.all()
    context = {
        "data": data
    }
    return render(request, "index.html", context)


def detail(request, pk):
    # try:
    #      data = BookModel.objects.get(pk=pk)
    # except BookModel.DoesNotExist:
    #     raise Http404
    book = get_object_or_404(BookModel, pk=pk)


    context = {
        "book": book
    }
    return render(request, "detail.html", context)