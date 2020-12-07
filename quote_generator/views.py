from django.shortcuts import render
from django.http import HttpResponse
import requests


def home(request):
    url = "https://favqs.com/api/qotd"
   
    response = requests.request("GET", url,)
    print(response.text)
    quotes = {}
    quotes['quote'] = response.json()['quote']['body']
    quotes['author'] = response.json()['quote']['author']
    return render(request, "home.html", quotes)  

def favouriteQuotes(request):
    return HttpResponse("favouriteQuotes")
