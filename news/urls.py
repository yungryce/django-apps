from django.urls import path
from . import views
# from .models import Article

app_name = 'news'

urlpatterns = [
    # path('', views.report, name='news'),
    path('articles/<int:year>/', views.year_archive),
    # path('articles/<int:year>/<int:month>/', views.month_archive),
    # path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]