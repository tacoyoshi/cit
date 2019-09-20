from django.urls import path
from . import views

app_name = 'stations'
urlpatterns = [
    path('', views.StationList.as_view(), name='station-list'),
    path('<int:pk>/', views.StationView.as_view(), name='station-detail'),
    path('add', views.StationCreate.as_view(), name='station-add'),
    path('<int:pk>/update', views.StationUpdate.as_view(), name='station-update'),
    path('<int:pk>/delete', views.StationDelete.as_view(), name='station-delete'),
]
