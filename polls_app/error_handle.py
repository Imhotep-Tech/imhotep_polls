from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden, HttpResponseBadRequest

def handler404(request, exception):
    context = {
        'error_code': '404',
        'error_description': "We can't find that page."
    }
    return render(request, 'error_handle.html', context, status=404)

def handler500(request):
    context = {
        'error_code': '500',
        'error_description': "Something went wrong."
    }
    return render(request, 'error_handle.html', context, status=500)

def handler403(request, exception):
    context = {
        'error_code': '403',
        'error_description': "Access Denied."
    }
    return render(request, 'error_handle.html', context, status=403)

def handler400(request, exception):
    context = {
        'error_code': '400',
        'error_description': "Bad Request."
    }
    return render(request, 'error_handle.html', context, status=400)