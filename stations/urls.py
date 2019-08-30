from django.urls import path
from . import views

app_name = 'stations'
urlpatterns = [
    path('', views.StationList.as_view(), name='station-list'),
    path('<int:pk>/', views.StationView.as_view(), name='station-detail'),
    path('station/add/', views.StationCreate.as_view(), name='station-add'),
    path('station/<int:pk>/', views.StationUpdate.as_view(), name='station-update'),
    path('station/<int:pk>/delete/', views.StationDelete.as_view(), name='station-delete'),
]
