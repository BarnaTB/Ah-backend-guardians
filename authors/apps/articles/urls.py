from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ArticleCreateListCreateView, ArticleDetailsView
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Articles API')

urlpatterns = [
    path('swagger-docs/', schema_view),
    path('articles/', ArticleCreateListCreateView.as_view(), name="create"),
    path('articles/<int:pk>/',
    ArticleDetailsView.as_view(), name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)