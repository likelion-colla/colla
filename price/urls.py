from django.urls import path
from price import views

app_name = "price"

urlpatterns = [
    path("", views.price_main, name="price_main"),
    path("/artist/", views.price_artist, name="price_artist"),  # 아티스트 id 나오면, url 수정 필요
]