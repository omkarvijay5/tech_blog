from django.conf.urls import url

from blog.api import ArticleListApi, RandomArticlesApi


urlpatterns = [
    url(r'^articles/$', ArticleListApi.as_view(), name='articles_api'),
    url(r'^random/articles/$', RandomArticlesApi.as_view(), name='articles_api'),
]
