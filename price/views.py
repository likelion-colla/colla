from django.shortcuts import render


def price_main(request):
    return render(request, "price/price-main.html")


def price_artist(request):
    return render(request, "price/price-artist.html")
