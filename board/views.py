from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from board.models import Post
from django.contrib.auth.models import User
from django.contrib import auth


def board_write(request):
    if request.method == "GET":
        return render(request, "board/board-write.html")
    elif request.method == "POST":
        if request.user.is_authenticated:
            new_post = Post()
            new_post.title = request.POST["title"]
            new_post.category = request.POST["category"]
            new_post.content = request.POST["content"]
            if request.FILES.get("image"):
                # new_post.head_image = request.FILES["image"]
                new_post.head_image = request.FILES.get("image")
            new_post.created_user = request.user
            new_post.save()
            return redirect("board:main")
        else:
            return redirect("accounts:login")


def board_main(request):
    post_list = Post.objects.all().order_by("-pk")
    context = {
        "post_list": post_list
    }
    return render(request, "board/board-main.html", context)


def board_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        "post": post
    }
    return render(request, "board/board-detail.html", context)


def board_edit(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        context = {
            "post": post
        }
        return render(request, "board/board-edit.html", context)
    elif request.method == "POST":
        post = Post.objects.get(id=post_id)
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.save()
        return HttpResponseRedirect(f"/board/detail/{post_id}/")


def board_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("board:main")

