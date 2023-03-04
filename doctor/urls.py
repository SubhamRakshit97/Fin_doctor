from django.urls import path
from .views import HomeTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView , ServicesTemplateView , TestimonialsTemplateView , TeamTemplateView

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("make-an-appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),
    path("services/", ServicesTemplateView.as_view(), name="services"),
    path("testimonials/", TestimonialsTemplateView.as_view(), name="testimonials"),
    path("team/", TeamTemplateView.as_view(), name="team"),



    
]
