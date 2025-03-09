import json

import requests
from django.shortcuts import render

from icecream_view import config


def admin_view(request):

    res = requests.get(config.API + "/commands")
    commands = json.loads(res.text)

    total_amount = 0.0
    for command in commands:
        total_amount += command["price"]

    res = requests.get(config.API + "/batchs")
    batchs = json.loads(res.text)

    return render(
        request,
        "admin.html",
        {
            "batchs": batchs,
            "commands": commands,
            "api": config.API,
            "totalAmount": total_amount,
        },
    )
