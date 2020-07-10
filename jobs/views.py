# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404

from .models import Job, Category

# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request, "jobs/home.html", {"jobs": jobs})


def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, "jobs/detail.html", {"job": job_detail})


def category_content(request, category_id):
    category = Category.objects.get(id=category_id)
    artworks = Job.objects.filter(category=category)
    return render(request, "jobs/gallery.html", {"jobs": artworks})


def show_category(request, hierarchy=None):
    category_slug = hierarchy.split("/")
    category_queryset = list(Category.objects.all())
    all_slugs = [x.slug for x in category_queryset]
    parent = None
    for slug in category_slug:
        if slug in all_slugs:
            parent = get_object_or_404(Category, slug=slug, parent=parent)
        else:
            instance = get_object_or_404(Job, slug=slug)
            breadcrumbs_link = instance.get_cat_list()
            category_name = [
                " ".join(i.split("/")[-1].split("-")) for i in breadcrumbs_link
            ]
            breadcrumbs = zip(breadcrumbs_link, category_name)
            return render(
                request,
                "detail.html",
                {"instance": instance, "breadcrumbs": breadcrumbs},
            )

    return render(
        request,
        "categories.html",
        {"post_set": parent.post_set.all(), "sub_categories": parent.children.all()},
    )

