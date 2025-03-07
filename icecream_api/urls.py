from django.urls import path

from icecream_api.views.batchs import BatchsListApiView, BatchRefillApiView
from icecream_api.views.commands import (
    CommandDetailApiView,
    CommandsListApiView,
    CommandSubmitApiView,
)
from icecream_api.views.items import ItemDetailApiView, ItemsListApiView

urlpatterns = [
    path("items", ItemsListApiView.as_view()),
    path("item/<int:item_id>", ItemDetailApiView.as_view()),
    path("command/submit", CommandSubmitApiView.as_view()),
    path("commands", CommandsListApiView.as_view()),
    path("command/<str:command_id>", CommandDetailApiView.as_view()),
    path("batchs", BatchsListApiView.as_view()),
    path("batch/refill/<str:batch_name>", BatchRefillApiView.as_view()),
]
