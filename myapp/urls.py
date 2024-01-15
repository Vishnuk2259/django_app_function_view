from django.urls import path
from . import views
 
urlpatterns = [
    path('create/', views.create_view, name='create'),
    path('list/', views.list_view, name='list'),  
    path('<id>/', views.detail_view, name='detail_list'),
    path('<id>/delete/', views.delete_view, name='delete'),
    path('<id>/update/', views.update_view, name='update'),
    path('', views.list_view),
    path('home', views.NewApp, name = 'home'),
]

