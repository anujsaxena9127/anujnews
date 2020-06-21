from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    news_api_request=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=3c2e1471a6514464a290269dd41f753b")
    api=json.loads(news_api_request.content)
    return render(request, 'index.html',{'api':api})