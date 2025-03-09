from django.forms import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from icecream_api.models.item_related import Item

from ..serializers import ItemSerializer


class ItemsListApiView(APIView):

    def get(self, request, *args, **kwargs):
        item = Item.objects.filter()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ItemDetailApiView(APIView):

    def get_object(self, item_id):
        try:
            return Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return None
        except ValidationError:
            return None

    def get(self, request, item_id, *args, **kwargs):
        item_instance = self.get_object(item_id)
        if not item_instance:
            return Response(
                {"res": "Object with item id does not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ItemSerializer(item_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
