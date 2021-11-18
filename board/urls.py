from django.urls import path
from board import views

app_name = "board"
urlpatterns = [
    path("", views.board_main, name="main"),
    path("detail/<int:post_id>/", views.board_detail, name="detail"),
    path("write/", views.board_write, name="write"),
    path("edit/<int:post_id>/", views.board_edit, name="edit"),
    path("delete/<int:post_id>/", views.board_delete, name="delete")



]