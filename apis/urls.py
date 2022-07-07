from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users, name='api-get-users'),
    # path('user/', views.get_user, name='api-get-user'),
    path('register/', views.register, name='api-register'),
    path('login/', views.login, name='api-login'),
    path('authenticated_user/', views.authenticated_user, name='api-authenticated-user'),
    path('logout/', views.logout, name='api-logout'),
    path('assessments/', views.get_assessments, name='api-get-assessments'),
    path('mcquestions/', views.get_mcquestions, name='api-get-mcq'),
    path('squestions/', views.get_squestions, name='api-get-sq'),
    path('kata/', views.get_kataquestions, name='api-get-kataq'),
    path('add_assessment/', views.add_assessment, name='api-add-assessment'),
]
