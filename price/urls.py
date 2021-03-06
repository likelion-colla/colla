from django.urls import path
from price import views

app_name = "price"

urlpatterns = [
    path("", views.price_main, name="main"),
    path("price/artist/", views.price_artist, name="artist"),  # 아티스트 id 나오면, url 수정 필요
]