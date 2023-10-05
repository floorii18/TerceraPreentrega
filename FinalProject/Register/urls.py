from django.urls import path, include
from Register import views

urlpatterns = [
    path('signin/', views.signin, name="signin"),
    path('login/', views.login_request, name="Login"),
    path('', include('FinalProjectApp.urls')),
]
