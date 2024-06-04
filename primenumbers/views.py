from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Number
from django.urls import reverse
import matplotlib.pyplot as plt
import math


# Create your views here.

def index(request):
    return render(request, "primenumbers/index.html")


def list(request):
    numbers = Number.objects.all()
    context = {"numbers": numbers}
    return render(request, "primenumbers/list.html", context)


def add(request):
    for x in range(70000, 100001):
        q = Number(number=x, isPrime=False)
        q.isPrime = q.TestisPrime()
        q.save()

    return HttpResponseRedirect(reverse("primenumbers:list"))


def searchbox(request):
    searched_number = int(request.POST["number_searched"])
    return HttpResponseRedirect(reverse("primenumbers:search", args=[searched_number]))


def search(request, numberInt):
    numb = Number(number=numberInt, isPrime=False)
    numb.isPrime = numb.TestisPrime()
    divs = numb.divisors()
    isEven = numb.isEven()
    isPerfect = numb.isPerfect()
    binary_version = numb.getbinary()[2:]

    return render(request, "primenumbers/detail.html",
                  {"number": numb, "divs": divs, "isEven": isEven, "isPerfect": isPerfect,
                   "binary_version": binary_version})


def fibonacci(request):
    return HttpResponse("TODO")


def collatz(request):
    if request.method == "POST":
        numbers = []
        number = int(request.POST["startnumber"])
        startnumber = request.POST["startnumber"]
        numbers.append(number)
        count = 0
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                numbers.append(number)
                count = count + 1
            else:
                number = 3 * number + 1
                numbers.append(number)
                count = count + 1

        plt.cla()
        plt.plot(range(len(numbers)), numbers)
        plt.savefig("primenumbers/static/collatz")

        return render(request, "primenumbers/collatz-result.html", {"startnumber": startnumber, "count": count})

    else:
        return render(request, "primenumbers/collatz.html")


def binomial(request):
    if request.method == "POST":
        numbers = []
        p = float(request.POST["p"])
        n = int(request.POST["n"])
        e = round(n * p, ndigits=2)
        s = round(math.sqrt(n * p * (1 - p)), ndigits=2)
        for x in range(0, n + 1):
            P = (math.factorial(n) / (math.factorial(x) * math.factorial(n - x))) * (p ** x) * (1 - p) ** (n - x)
            numbers.append(P)

        plt.cla()
        plt.plot(range(len(numbers)), numbers)
        plt.savefig("primenumbers/static/binomial")
        return render(request, "primenumbers/binomial-result.html", {"e": e, "s": s})

    else:
        return render(request, "primenumbers/binomial.html")


def average(request):
    return HttpResponse("TODO")


def quiz(request):
    if request.method == "POST":
        points = 0
        if request.POST["q1"] == "111111111":
            points = points + 1
        if request.POST["q2"] == "one":
            points = points + 1
        if request.POST["q3"] == "Rayo's Number":
            points = points + 1
        if request.POST["q4"] == "infinity" or request.POST["q4"] == "-1/12":
            points = points + 1
        if request.POST["q5"] == "magic" or request.POST["q5"] == "don't make no sense, stupid question" or \
                request.POST["q5"] == "i":
            points = points + 1
        if request.POST["q6"] == "all mentioned answers plus one":
            points = points + 1

        match points:
            case 6:
                answer = "You're a genius!"
            case 5:
                answer = "Impressive!"
            case 4:
                answer = "You've got potential, keep going!"
            case 3:
                answer = "You can do better!"
            case 2:
                answer = "Why are you on a math website, when you're so dumb?"
            case 1:
                answer = "Congratulations! You are very good at making other people feel smart!"
            case 0:
                answer = "How do you survive?"
        return render(request, "primenumbers/quiz-result.html", {"points": points, "answer": answer})

    else:
        return render(request, "primenumbers/quiz.html")


def crypto(request):
    return render(request, "primenumbers/crypto.html")
