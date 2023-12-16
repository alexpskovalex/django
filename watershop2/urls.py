from django.urls import path

from . import views

urlpatterns = [
    path("", views.about, name="index"),
    path("about/", views.about, name="about"),
    path("links/", views.links, name="about"),
    path("pool/", views.pool, name="about"),
]
