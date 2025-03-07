from django.urls import include, path

from icecream_api.views.batchs import BatchListApiView, BatchRefillApiView
from icecream_api.views.commands import (CommandDetailApiView,
                                         CommandListApiView,
                                         CommandSubmitApiView)
from icecream_api.views.items import ItemDetailApiView, ItemListApiView

urlpatterns = [
    path("items", ItemListApiView.as_view()),
    path("item/<int:item_id>", ItemDetailApiView.as_view()),
    path("command/submit", CommandSubmitApiView.as_view()),
    path("commands", CommandListApiView.as_view()),
    path("command/<str:command_id>", CommandDetailApiView.as_view()),
    path("batchs", BatchListApiView.as_view()),
    path("batch/refill/<str:batch_name>", BatchRefillApiView.as_view()),
]
