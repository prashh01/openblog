from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('add/', views.add, name="add"),
    path('update/<int:id>',views.update, name="update"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('report/', views.report, name='report'),
]
