from django.conf.urls.static import static
from django.urls import path

from icecream import settings
from icecream_view.views.admin import admin_view
from icecream_view.views.command import commande_view
from icecream_view.views.retrieve_command import retrieve_command_view

urlpatterns = [
    path("", commande_view, name="command"),
    path("retrieve/", retrieve_command_view, name="retrieve_command"),
    path("admin/", admin_view, name="admin"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
