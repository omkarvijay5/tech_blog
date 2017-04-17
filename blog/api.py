# django imports
from rest_framework import generics

# third party imports
from blog.models import Article
from blog.serializers import ArticleSerializer


class ArticleListView(generics.ListAPIView):
    """
    Returns a list of all authors.
    """
    model = Article
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().select_related('author').order_by('pub_date')[:10]
