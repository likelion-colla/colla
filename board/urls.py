from django.urls import path
from board import views

app_name = "board"
urlpatterns = [
    path("", views , name="board-main"),
    path("/detail/", views , name="board-detail"), #나중에 detail 지우고 <id:post_id>로 바꾸기
    path("/write/", views , name="board-write"),


]