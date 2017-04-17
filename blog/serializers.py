# python imports
from datetime import datetime

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

    def to_representation(self, article):
        rep = super(ArticleSerializer, self).to_representation(article)

        # convert pub datetime to proper weekday, month date year format
        pub_date = rep['pub_date']
        rep['pub_date'] = datetime.strptime(pub_date, "%Y-%m-%dT%H:%M:%SZ").strftime("%A, %B %d %Y")

        # get the authors first name and last name or username
        author = article.author
        rep['author'] = author.get_full_name() or author.username
        return rep
