from django.conf.urls import url

from blog.api import Article


urlpatterns = [
    url(r'^articles/$', ArticleListView.as_view(), name='articles'),
]
