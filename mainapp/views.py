from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def health(request):
    return render(request, 'cards/health.html')

def nutrition(request):
    return render(request, 'cards/nutrition.html')

def career(request):
    return render(request, 'cards/career.html')

def life(request):
    return render(request, 'cards/life.html')

def family(request):
    return render(request, 'cards/family.html')

def sports(request):
    return render(request, 'cards/sports.html')

def profile_view(request):
    return render(request, 'cards/profile.html')
