from django.shortcuts import render, redirect
from django.http import HttpResponse
from .app.forms import CallbackForm, CommentForm
from django.http import HttpRequest, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from django.contrib.auth import login
from django.db import models
from .models import Blog, Comment


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def about(request):
    return render(request, "about.html")


def links(request):
    return render(request, "links.html")


def pool(request: HttpRequest):
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            # return JsonResponse{"true":True}
            return render(request, "pool.html", {"result": form.cleaned_data})
            # return HttpResponseRedirect("/about/")
    else:
        form = CallbackForm()
    return render(request, "pool.html", {"form": form})


def registration(request):
    """Renders the registration page."""

    assert isinstance(request, HttpRequest)
    regform = UserCreationForm(request.POST or None)
    if request.method == "POST":  # после отправки формы
        if regform.is_valid():  # валидация полей формы
            reg_f = regform.save(
                commit=False
            )  # не сохраняем автоматически данные формы

            reg_f.is_staff = False  # запрещен вход в административный раздел
            reg_f.is_active = True  # активный пользователь

            reg_f.is_superuser = False  # не является суперпользователем

            reg_f.date_joined = datetime.now()  # дата регистрации

            reg_f.last_login = datetime.now()  # дата последней авторизации

            reg_f.save()  # сохраняем изменения после добавления данных
            reg_f.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, reg_f)
            return redirect("/")  # переадресация на главную страницу после регистрации
        # else:
        #     date = datetime.now()
        #     return render(
        #         request,
        #         "registration.html",
        #         {
        #             "regform": regform,  # передача формы в шаблон веб-страницы
        #             "year": date.year,
        #         },
        #     )
    # else:
    date = datetime.now()
    # regform = (
    #     UserCreationForm()
    # )  # создание объекта формы для ввода данных нового пользователя

    return render(
        request,
        "registration.html",
        {"regform": regform, "year": date.year},  # передача формы в шаблон веб-страницы
    )


# def login(request):
#     return render(request, "login.html")
def blog(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    posts = Blog.objects.all()  # запрос на выбор всех статей блога из модели
    return render(
        request,
        "blog.html",
        {
            "title": "Блог",
            "posts": posts,  # передача списка статей в шаблон веб-страницы
            "year": datetime.now().year,
        },
    )


def blogpost(request, parametr):
    """Renders the blogpost page."""
    assert isinstance(request, HttpRequest)
    form = CommentForm(request.POST or None)
    post_1 = Blog.objects.get(
        id=parametr
    ) 
    if request.method == "POST":  # после отправки данных формы на сервер методом POST
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = (
                request.user
            )  # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя
            comment_f.date = (
                datetime.now()
            )  # добавляем в модель Комментария (Comment) текущую дату
            comment_f.blog_id = Blog.objects.get(
                id=parametr
            )  # добавляем в модель Комментария (Comment) статью, для которой данный комментарий
            comment_f.save()  # сохраняем изменения после добавления полей
            return redirect(
                "blogpost", parametr=post_1.id
            )  # переадресация на ту же страницу статьи после отправки комментария
        # else:
        #     form = CommentForm()  # создание формы для ввода комментария
 # запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(blog_id=parametr)
    return render(
        request,
        "blogpost.html",
        {
            "form": form,
            "post_1": post_1,  # передача конкретной статьи в шаблон веб-страницы
            "year": datetime.now().year,
            "comments": comments,
        },
    )
