from django.conf.urls import url

from blog.api import ArticleListView


urlpatterns = [
    url(r'^articles/$', ArticleListView.as_view(), name='articles_api'),
]
