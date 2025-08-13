from django.shortcuts import render


def error_401(request, exception=None):
    return render(request, 'Admin/errors/401.html', {'exception': exception}, status=401)


def error_403(request, exception=None):
    return render(request, 'Admin/errors/403.html', {'exception': exception}, status=403)


def error_404(request, exception=None):
    return render(request, 'Admin/errors/404.html', {'exception': exception}, status=404)


def error_500(request, exception=None):
    return render(request, 'Admin/errors/500.html', {'exception': exception}, status=500)
