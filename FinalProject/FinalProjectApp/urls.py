from django.urls import path
from FinalProjectApp import views

urlpatterns = [
    path('', views.Home, name=""),
    path('experience/', views.Experience, name="experience"),
    path('certifications/', views.Certifications, name="certifications"),
    path('skills/', views.Skill, name="skills"),
    path('about/', views.About, name="about"),
    path('listskills', views.addskill, name="listskills")
]
