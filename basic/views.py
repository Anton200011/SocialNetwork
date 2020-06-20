from django.shortcuts import render


# Create your views here.

# "Стартовая" страница
def start_view(request):
    return render(request, "start.html")
