from django.shortcuts import render
from django.http.response import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
articles = {
  "sports":"Sports page",
  "esports": "Esports page",
  "politics": "Politics page",
  "arts":"Arts Page"
}

# def sports_view(request):
#   return HttpResponse(articles["sports"])
# 
# def finance_view(request):
#   return HttpResponse(articles["finance"])

def news_view(request,topic):
  try:
    return HttpResponse(articles[topic])
  except:
    raise Http404("Page Not Found For This Topic")

# def add_view(request , num1, num2):
#   # result = num1 + num2
#   result = f"Sum of {num1} and {num2} is {num1 + num2}"
#   return HttpResponse(str(result))

def num_page_view(request,num_page):
  try:
    topic_list = list(articles.keys())
    topic = topic_list[num_page]
    return HttpResponseRedirect(reverse('topic-page',args=[topic]))
  except:
    raise Http404("Page Not Found For This Topic")

