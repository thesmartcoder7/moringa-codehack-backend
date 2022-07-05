from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users, name='api-get-users'),
    path('assessments/', views.get_assessments, name='api-get-assessments'),
    path('mcquestions/', views.get_mcquestions, name='api-get-mcq'),
    path('squestions/', views.get_squestions, name='api-get-sq'),
    path('kata/', views.get_kataquestions, name='api-get-kataq'),
    path('add_assessment/', views.add_assessment, name='api-add-assessment'),
]
