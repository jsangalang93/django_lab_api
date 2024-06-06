from django.urls import path
from . import views

urlpatterns = [
    path('api/companies/', views.companiesList.as_view(), name='companies_list'),
    path('api/companies/<int:pk>', views.companiesDetail.as_view(), name='companies_detail'),
    path('api/locations/', views.locationsList.as_view(), name='locations_list'),
    path('api/locations/<int:pk>', views.locationsDetail.as_view(), name='locations_detail'),
]