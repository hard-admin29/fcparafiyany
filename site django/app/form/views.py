from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.core.mail import send_mail as django_send_mail
from django.conf import settings

from enum import Enum
import asyncio


class ValidState(Enum):
    man: str = "Чоловік"
    woman: str = "Жінка"


class ValidPosition(Enum):
    at = "Нападающий"
    center = "Півзахисник"
    df = "Захисник"
    gk = "Воротарь"


def form(request) -> render:
    error = ""

    blocked_users_for_ip = [

    ]

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        user_ip_address = x_forwarded_for.split(',')[0]
    else:
        user_ip_address = request.META.get('REMOTE_ADDR')

    if user_ip_address in blocked_users_for_ip:
        return HttpResponseForbidden(render(request, "main/page-blocked.html", {"ip_address": user_ip_address}))

    if request.method == "POST":
        try:
            email: str = request.POST.get("email")
            address: str = request.POST.get("address")
            name: str = request.POST.get("name")
            last_name: str = request.POST.get("lastName")
            city: str = request.POST.get("city")
            state: ValidState = ValidState(request.POST.get("state").title())
            position: ValidPosition = ValidPosition(request.POST.get("position").title())


            if (
                email.endswith("@gmail.com") or
                email.endswith("@mail.com") or
                email.endswith("@email.com")
            ):
                if address != "" and name != "" and last_name != "" and city != "":
                    asyncio.run(send_mail(user_email=email, address=address, name=name,
                        last_name=last_name, city=city, state=state.value,
                        position=position.value, user_ip=user_ip_address))

                else:
                    error = "Ви неправильно заповнили форму"
            else:
                error = "Ви неправильно заповнили форму"
        except:
            error = "Ви неправильно заповнили форму"

    return render(request, 'form/form.html', {"error": error})


async def send_mail(user_email: str,
                    address: str,
                    name: str,
                    last_name: str,
                    city: str,
                    state: str,
                    position: str,
                    user_ip: str = None) -> str | None:
    """
    This is func get user info from
    form and send to email address admins
    :param user_email: mail user (type str and endswith @gmail.com or @email.com)
    :param address: user address (type str)
    :param name: str
    :param last_name: str
    :param city: str
    :param state: Get validation for class ValidState
    :param position: Get validation for class ValidPosition
    :param user_ip: user ip address get for if user send in form bad information user blocked at site
    :return:
    """
    sender = settings.EMAIL_HOST_USER
    recipients = ['danylo29bro@gmail.com', 'maksimkozij67@gmail.com']

    subject = 'Нова Анкета!'
    message = F"""
    Електронна адреса: {user_email}
    Адреса: {address}
    Ім'я: {name}
    Прізвище: {last_name}
    Місто: {city}
    Стать: {state}
    Позиція: {position}
    IP користувача: {user_ip}
    """

    try:
        django_send_mail(subject, message, sender, recipients)
        return 'Повідомлення відправлено успішно'
    except Exception as ex:
        return f'Помилка відправки: {str(ex)}'

