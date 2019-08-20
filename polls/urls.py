from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/<int:article_id>/', views.article_page, name='article_page'),
    path('edit/', views.edit_page, name='edit_page'),
    path('edit/action', views.edit_action, name='edit_action'),
]
