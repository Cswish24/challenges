from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
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
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("please select an address with a correct coresponding month")


