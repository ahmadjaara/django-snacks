from django.urls import path
from .views import Aboutpage, Contactpage, Homepage

urlpatterns =[
    path("",Homepage.as_view(),name="home"),
    path("about",Aboutpage.as_view(),name="about"),
    path("contact",Contactpage.as_view(),name="contact")
    ]