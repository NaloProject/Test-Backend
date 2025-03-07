from django.forms import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from icecream_api.models.item_related import Item

from ..serializers import ItemSerializer


class ItemListApiView(APIView):

    def get(self, request, *args, **kwargs):
        """
        List all the todo items for given requested user
        """
        item = Item.objects.filter()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ItemDetailApiView(APIView):

    def get_object(self, item_id):
        """
        Helper method to get the object with given todo_id, and user_id
        """
        try:
            return Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return None
        except ValidationError:
            return None

    def get(self, request, item_id, *args, **kwargs):
        """
        Retrieves the Item with given item_id
        """
        item_instance = self.get_object(item_id)
        if not item_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = ItemSerializer(item_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
