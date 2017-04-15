# third party imports
from rest_framework import serializers

from blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializing all the Articles
    """
    class Meta:
        model = Article
        fields = '__all__'
