from django.shortcuts import render


def start_page(request):
    return render(request, 'start page.html')


def contact_(request):
    return render(request, 'contact page.html')


def reviews(request):
    return render(request, 'reviews page.html')
