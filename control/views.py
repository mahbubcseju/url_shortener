from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from .models import StoreUrl
from .service import generate_shortened_url, shortened_url


# Create your views here.
def generate_short_url(request):
    form = forms.GivenUrl(request.POST or None)
    if form.is_valid():
        form.save()
        result = {
            "url": form.cleaned_data["given_url"],
            "value": generate_shortened_url(form.cleaned_data["given_url"]),
        }
        return render(request, "result.html", result)
    return render(request, "home.html", {"form": form})


def get_shortened_url(request, pk):
    url = shortened_url(int(pk))
    return redirect(url)
