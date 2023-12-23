from datetime import datetime
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .app.forms import BootstrapAuthForm
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path("", views.about, name="index"),
    path("about/", views.about, name="about"),
    path("video/", views.video, name="video"),
    path("about_us/", views.about_us, name="about_us"),
    path("contact/", views.contact, name="contact"),
    path("links/", views.links, name="links"),
    path("pool/", views.pool, name="pool"),
    path("new_blog/", views.new_blog, name="new_blog"),
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
    path("blog/", views.blog, name="blog"),
    path("blogpost/<int:parametr>/", views.blogpost, name="blogpost"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
