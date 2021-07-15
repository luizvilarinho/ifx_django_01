from django.urls import path, include
from .views import CompanyViewSet, ModelViewSet, EmployeeViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('company', CompanyViewSet, basename='Company')
router.register('departaments', ModelViewSet, basename='Departaments')
router.register('employee', EmployeeViewSet, basename='Employee')


urlpatterns = [
    path('', include(router.urls)),

]