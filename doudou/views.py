import json
import requests
from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, 'doudou/home.html')


def book_info_search(request):
    book_sn = request.GET.get("sn")
    url = "http://book.feelyou.top/isbn/{}".format(book_sn)
    data = requests.get(url)
    return JsonResponse({"result": True, "data": json.loads(data.content)})
