from django.shortcuts import render
from .models import Visit

# Create your views here.
def index(request, page=""):
    v = Visit(page=page)

    if request.user.is_authenticated:
        v.username = request.user.username
    v.save()

    visiors = Visit.objects.filter(page=page)
    context = {
        "page":page,
        "visitors":visiors,
        "num_visits": visiors.count()
    }

    return render(request, "index.html", context=context)
