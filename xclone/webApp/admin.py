from django.contrib import admin

# Register your models here.
from .models import Article, Writer, ArticleWriter


admin.site.register(Writer)


class ArticleWriterInline(admin.TabularInline):
    model = ArticleWriter
    extra = 0   
    # By default, Django provides three blank forms for adding related objects in an inline form.
    # extra = 1: This tells Django to display 1 empty form for adding a new ArticleWriter object. By 
    # default, this value is set to 3, which is why you're seeing three blank forms.


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ArticleWriterInline,
    ]


admin.site.register(Article, ArticleAdmin)


