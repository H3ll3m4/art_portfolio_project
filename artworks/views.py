from django.shortcuts import render
from artworks.models import Artwork  # , Comment

# from .forms import CommentForm

# Create your views here.


def artwork_index(request):
    artworks = Artwork.objects.all()
    context = {"artworks": artworks}
    return render(request, "artwork_index.html", context)


def artwork_category(request, category):
    artworks = Artwork.objects.filter(categories__name__contains=category)
    context = {"category": category, "artworks": artworks}
    return render(request, "artwork_category.html", context)


def artwork_detail(request, pk):
    artwork = Artwork.objects.get(pk=pk)
    # form = CommentForm()

    # if request.method == "POST":
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = Comment(
    #             author=form.cleaned_data["author"],
    #             body=form.cleaned_data["body"],
    #             artwork=artwork,
    #         )
    #         comment.save()

    # comments = Comment.objects.filter(artwork=artwork)
    # context = {
    #     "artwork": artwork,
    #     "comments": comments,
    #     "form": form,
    # }
    context = {"artwork": artwork}
    return render(request, "artwork_detail.html", context)

