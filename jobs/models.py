# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200)
    # category = models.CharField(max_length=50)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True, null=True
    )
    price = models.PositiveSmallIntegerField(null=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.summary

    def get_cat_list(self):
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb) - 1):
            breadcrumb[i] = "/".join(breadcrumb[-1 : i - 1 : -1])
        return breadcrumb[-1:0:-1]


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True, related_name="children"
    )

    class Meta:
        unique_together = (
            "slug",
            "parent",
        )
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return " -> ".join(full_path[::-1])

