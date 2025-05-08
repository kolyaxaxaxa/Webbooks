from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 127.0.0.1:8000/  www.site.ru/

    path('book/<int:book_id>/', views.book_by_id),  # site.ru/book/17
    path('book/<slug:book_slug>/', views.book_by_slug),  # site.ru/book/puskin-2


]
