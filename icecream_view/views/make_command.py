import json

import requests
from django.shortcuts import render

from icecream_view import config


def make_command_view(request):

    res = requests.get(config.API + "/items")
    flavours = json.loads(res.text)

    return render(
        request,
        "make_command.html",
        {"flavours": flavours, "api": config.API},
    )
