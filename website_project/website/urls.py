from django.urls import path
from website import views

urlpatterns =[
    path('',views.index,name='home'),
    path('send_email',views.volunteer_Email,name='send_email')


]
