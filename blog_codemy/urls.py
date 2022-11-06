from django.urls import path
# from . import views
from .views import DetailV, Homeview, Formview

# app_name = 'blog' not working when name added to path

urlpatterns = [
    # path('', views.index, name='index'),
    path('', Homeview.as_view(), name='home'),
    path('<int:pk>/', DetailV.as_view(), name='details'),
    path('forms', Formview.as_view(), name='forms'),
]