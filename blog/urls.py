from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),  # yoki home_page
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
    path('today/', views.today_posts, name='today_posts'),
    path('top/', views.top_posts, name='top_posts'),
    path('search/' , views.search_results , name='search_results'),

]
