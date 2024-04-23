from django.urls import path,include
from .import views
app_name ='project_main'

urlpatterns = [
    path('',views.customer,name='customer'),
    path('librarian/',views.librarian,name='librarian'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login')
]
