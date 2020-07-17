from django.contrib import admin
from .models import Artwork, Category  # , Comment

# Register your models here.


class ArtworkAdmin(admin.ModelAdmin):
    list_display = ["title", "info", "price", "slug",]
    #pass


class CategoryAdmin(admin.ModelAdmin):
    pass


# class CommentAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Comment, CommentAdmin)
