from django.urls import path
from . import views

app_name = 'geotree'
urlpatterns = [
    path('', views.geotree, name='geo_select'),
    path('geo/<str:geoname>/', views.DetailView.as_view(), name = 'details'),
    path('geo/', views.geo_selected, name='geo_selected')
]