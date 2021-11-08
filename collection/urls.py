from django.urls import path
from board import views

app_name = "collection"
urlpatterns = [
    path("", views , name="main"),
    path("detail/", views , name="detail"), # 나중에 detail 지우고 <id:item_id>로 바꾸기
    path("upload/", views , name="upload"),
    path("following/", views , name="following"), # 나중에 /following 앞에 <id:user_id> 붙이기
    path("user/", views , name="user"), # 나중에 /user 지우고 <id:user_id> 붙이기



]