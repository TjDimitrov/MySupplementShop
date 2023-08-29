from django.urls import path, include
from ExamProject.common import views

urlpatterns = (
    path('', views.homepage, name='homepage'),
    path('about/', views.about_us, name='about'),
    path('team/', views.team_information, name='team'),
    path('contacts/', views.contact_us, name='contacts'),
    path('team-control', views.team_control, name='team-control'),
    path('team-control/add', views.add_team_member, name='add team member'),
    path('team-control/<int:pk>/', include([
        path('edit/', views.edit_team_member, name='edit team member'),
        path('delete/', views.delete_team_member, name='delete team member')
    ]))
)
