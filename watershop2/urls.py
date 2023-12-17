from datetime import datetime
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .app.forms import BootstrapAuthForm
urlpatterns = [
    path("", views.about, name="index"),
    path("about/", views.about, name="about"),
    path("links/", views.links, name="links"),
    path("pool/", views.pool, name="pool"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html",
            extra_context={"title": "Вход", "year": datetime.now().year},
            authentication_form=BootstrapAuthForm,
        ),
        name="login",
    ),
    # path("login/", views.login, name="login"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="logout.html"),
        name="logout",
    ),
    path("registration/", views.registration, name="registration"),
]
