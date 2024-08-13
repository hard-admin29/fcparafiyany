from django.shortcuts import render
from django.http import HttpResponseForbidden


def main(request) -> render:
    blocked_users_for_ip = [

    ]
    user_ip_address = None
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        user_ip_address = x_forwarded_for.split(',')[0]
    else:
        user_ip_address = request.META.get('REMOTE_ADDR')

    if user_ip_address in blocked_users_for_ip:
        return HttpResponseForbidden(render(request, "main/page-blocked.html", {"ip_address": user_ip_address}))

    return render(request, "main/index.html")
