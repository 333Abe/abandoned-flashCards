from django.shortcuts import render

def index(request):
    """flashCards home page"""
    return render(request, 'flash_cards/index.html')
