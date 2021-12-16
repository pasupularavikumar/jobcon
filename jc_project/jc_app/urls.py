from django.urls import path
from . import views 
urlpatterns =[
    path('',views.home,name='home'),
    path('jobs/',views.jobs,name='jobs'),
    path('register/',views.register,name='register'),
    path('contact/',views.contact,name='contact'),
    path('jobs/<int:id>/',views.JobDetails,name='JobDetails'),
]