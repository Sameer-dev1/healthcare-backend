from django.urls import path
from .views import (
    RegisterView, LoginView,
    PatientListCreateView, PatientDetailView,
    DoctorListCreateView, DoctorDetailView,
    MappingListCreateView, MappingByPatientView, MappingDeleteView
)

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', LoginView.as_view()),

    path('patients/', PatientListCreateView.as_view()),
    path('patients/<int:pk>/', PatientDetailView.as_view()),

    path('doctors/', DoctorListCreateView.as_view()),
    path('doctors/<int:pk>/', DoctorDetailView.as_view()),

    path('mappings/', MappingListCreateView.as_view()),
    path('mappings/<int:patient_id>/', MappingByPatientView.as_view()),
    path('mappings/delete/<int:pk>/', MappingDeleteView.as_view()),
]
