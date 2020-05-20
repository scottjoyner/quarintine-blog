from . import views
from django.urls import include

from django.urls import path
from .feeds import LatestPostsFeed, AtomSiteNewsFeed #, AboutFeed

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList.as_view(), name="home"),
    # path("/about", AboutFeed(), name="about"),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]

