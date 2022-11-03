
from django.shortcuts import redirect, render
from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'main.html')


def send_to_main(request):
    return redirect(main)


def sub1(request):
    return render(request, 'sub1.html')


def sub2(request):
    return render(request, 'sub2.html')


def sub3(request):
    return render(request, 'sub3.html')
