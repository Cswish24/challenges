from urllib import response
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january": "Eat your weight in beef",
    "february": "Drink 200 eggs",
    "march": "Barbeque 20 chickens",
    "april": "Eat your weight in beef",
    "may": "Drink 200 eggs",
    "june": "Barbeque 20 chickens",
    "july": "Eat your weight in beef",
    "august": "Drink 200 eggs",
    "september": "Barbeque 20 chickens",
    "october": "Eat your weight in beef",
    "november": "Drink 200 eggs",
    "december": "Barbeque 20 chickens"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("please select a month that exists")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month.capitalize()
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        raise Http404()


