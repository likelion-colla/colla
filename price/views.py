from django.shortcuts import render
from price.models import ArtWork


def price_main(request):
    arts = ArtWork.objects.all()
    context = {
        "arts": arts
    }
    return render(request, "price/price-main.html", context)


def price_artist(request):
    return render(request, "price/price-artist.html")