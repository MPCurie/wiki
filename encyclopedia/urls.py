from django.urls import path

from . import views

app_name = 'encyclopedia'
urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('create_page', views.create_page, name='create_page'),
    path('random_page', views.random_page, name='random_page'),
    path('<str:entry>', views.content, name='entry'),
    path('<str:entry>/edit', views.edit_page, name='edit_page')
]
