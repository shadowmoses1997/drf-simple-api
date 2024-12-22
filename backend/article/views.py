from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from .models import Article
from .serializers import ArticleSerializer


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer