from django.urls import path

from . import views

app_name = "primenumbers"
urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.list, name="list"),
    path("add", views.add, name="add"),
    path("<int:numberInt>", views.search, name="search"),
    path("searchbox", views.searchbox, name="searchbox"),
    path("collatz", views.collatz, name="collatz"),
    path("binomial", views.binomial, name="binomial"),
    path("quiz", views.quiz, name="quiz"),
    path("crypto", views.crypto, name="crypto")
]
