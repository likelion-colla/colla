import requests
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def sign_up(request):
    context = {

    }
    if request.method == "POST":
        if (request.POST.get("username") and
                request.POST.get("password") and
                request.POST.get("password_check") == request.POST.get("password")):
            new_user = User.objects.create_user(
                username=request.POST.get("username"),
                password=request.POST.get("password")
            )
            auth.login(request, new_user)
            return redirect("price:main")
        else:
            context["error"] = "올바르지 않은 정보입니다."

    return render(request, "accounts/sign-up.html", context)


def login(request):
    context = {

    }
    if request.method == "POST":
        if request.POST.get("username") and request.POST.get("password"):
            user = auth.authenticate(
                request,
                username=request.POST.get("username"),
                password=request.POST.get("password"),
            )

            if user is not None:
                auth.login(request, user)
                return redirect("price:main")
            else:
                context["error"] = "아이디와 비밀번호를 다시 확인해주세요."
        else:
            context["error"] = "아이디와 비밀번호를 다시 확인해주세요."
    return render(request, "accounts/login.html", context)


def logout(request):
    if request.method == "POST" and request.user.is_authenticated:
        auth.logout(request)

    return redirect("price:main")
