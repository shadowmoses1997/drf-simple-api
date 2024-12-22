from django.urls import path
from .views import ArticleDetail, ArticleList



app_name = 'article'

urlpatterns = [
    path('', ArticleList.as_view(), name='ArticleList'),
path('<int:pk>', ArticleDetail.as_view(), name='ArticleDetail'),
]