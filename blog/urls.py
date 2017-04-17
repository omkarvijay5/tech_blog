from django.conf.urls import url

from blog.api import ArticleListApi, RandomArticlesApi, ArticleDetailApi


urlpatterns = [
    url(r'^articles/$', ArticleListApi.as_view(), name='articles_api'),
    url(r'^article/(?P<id>[0-9]+)/$', ArticleDetailApi.as_view(), name='article_detail_api'),
    url(r'^random/articles/$', RandomArticlesApi.as_view(), name='articles_api'),
]
