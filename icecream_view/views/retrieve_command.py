from django.shortcuts import render

from icecream_view import config


def retrieve_command_view(request):

    return render(
        request,
        "retrieve_command.html",
        {"api": config.API},
    )
