from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path("home/", views.home, name="home"),
path("articles/", views.article, name="article"),
path("article/<slug:article_slug>/", views.articleDetail, name="article_detail"),
path("writers/<int:writer_id>/", views.writerDetail, name="writer_detail"),
path('writers/', views.writer, name='writer'),
path('aboutus/', views.aboutus, name='aboutus'),
path('search/', views.search, name='search'),
path('delete/<int:comment_id>/', views.deleteComment, name='deleteComment'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)