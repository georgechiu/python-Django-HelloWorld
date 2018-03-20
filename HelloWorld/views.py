# -*- coding: utf-8 -*-

from django.shortcuts import render


def index(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'hello.html', context)