# python imports
import random

# django imports
from rest_framework import generics
from rest_framework.mixins import RetrieveModelMixin

# third party imports
from blog.models import Article
from blog.serializers import ArticleSerializer


class ArticleListApi(generics.ListAPIView):
    """
    Returns a list of top ten articles.
    """
    model = Article
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().select_related('author').order_by('pub_date')[:10]


class RandomArticlesApi(generics.ListAPIView):
    """
    Returns a list of all random articles.
    """
    model = Article
    serializer_class = ArticleSerializer

    def get_queryset(self):
        articles = list(self.model.objects.all().select_related('author'))
        random.shuffle(articles)
        return articles


class ArticleDetailApi(generics.RetrieveAPIView):
    """
    detail endpoint of article
    """
    lookup_field = 'id'
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
