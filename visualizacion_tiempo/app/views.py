from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime


def index(request):
    context = {
        "fecha": strftime("%d %b, %Y", localtime()),
        "hora": strftime("%H:%M %p", localtime())
    }    
    return render(request, "index.html", context)




