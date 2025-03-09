from django.forms import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from icecream_api.models.item_related import Batch

from ..serializers import BatchSerializer


class BatchsListApiView(APIView):

    def get(self, request, *args, **kwargs):
        batch = Batch.objects.filter()
        serializer = BatchSerializer(batch, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BatchRefillApiView(APIView):

    def get_object(self, batch_name: str):
        try:
            return Batch.objects.get(name=batch_name)
        except Batch.DoesNotExist:
            return None
        except ValidationError:
            return None

    def get(self, request, batch_name, *args, **kwargs) -> Response:
        command_instance = self.get_object(batch_name)
        if not command_instance:
            return Response(
                {"res": "Object with batch name does not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )
        command_instance.refill(full=True)
        serializer = BatchSerializer(command_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
