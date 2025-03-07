from django.forms import ValidationError
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from icecream_api.models.item_related import Batch, Item

from ..serializers import BatchSerializer


class BatchListApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the todo items for given requested user
        """
        batch = Batch.objects.filter()
        serializer = BatchSerializer(batch, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BatchRefillApiView(APIView):
    def get_object(self, batch_name):
        """
        Helper method to get the object with given todo_id, and user_id
        """
        try:
            return Batch.objects.get(name=batch_name)
        except Batch.DoesNotExist:
            return None
        except ValidationError:
            return None

    def get(self, request, batch_name, *args, **kwargs):
        """
        Retrieves the Command with given command_id
        """
        command_instance = self.get_object(batch_name)
        if not command_instance:
            return Response(
                {"res": "Object with batch name does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        command_instance.refill(full=True)
        serializer = BatchSerializer(command_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
