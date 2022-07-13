from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users, name='api-get-users'),
    path('all_students/', views.get_all_students, name='api-students'),
    path('student_data/', views.get_student_data, name='api-get-student-data'),
    path('register/', views.register, name='api-register'),
    path('login/', views.login, name='api-login'),
    path('authenticated_user/', views.authenticated_user, name='api-authenticated-user'),
    path('logout/', views.logout, name='api-logout'),
    path('assessments/', views.get_assessments, name='api-get-assessments'),
    path('mcquestions/', views.get_mcquestions, name='api-get-mcq'),
    path('mcanswers/', views.get_mcanswers, name='api-get-mca'),
    path('squestions/', views.get_squestions, name='api-get-sq'),
    path('kata/', views.get_kataquestions, name='api-get-kataq'),
    path('kata_tests/', views.get_katatests, name='api-get-katat'),
    path('feedback/', views.get_feedback, name='api-get-feedback'),
    path('invites/', views.get_invites, name='api-get-invites'),
    path('add_assessment/', views.add_assessment, name='api-add-assessment'),
    path('add_feedback/', views.add_feedback, name='api-add-feedback'),
    path('add_invite/', views.add_invite, name='api-add-invite'),
    path('run_code/', views.run_code, name='api-run-code'),
]
