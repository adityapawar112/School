from django.urls import path
from preschool import views

urlpatterns = [
    path('error404/', views.error404, name='error404'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('call_to_action/', views.call_to_action, name='call_to_action'),
    path('classes/', views.classes, name='classes'),
    path('contact/', views.contact, name='contact'),
    path('facility/', views.facility, name='facility'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),

]