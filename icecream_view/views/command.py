import json
import os

import requests
from django.shortcuts import render
from django.templatetags.static import static

from icecream import settings
from icecream_view import config


def commande_view(request):

    res = requests.get(config.API + "/items")
    flavours = json.loads(res.text)
    path = settings.STATIC_ROOT

    return render(
        request,
        "command.html",
        {"flavours": flavours, "api": config.API},
    )
