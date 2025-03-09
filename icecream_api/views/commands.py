from django.forms import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from icecream_api.models.command_related import Command

from ..serializers import CommandSerializer


class CommandsListApiView(APIView):

    def get(self, request, *args, **kwargs):
        command = Command.objects.filter().order_by("-created_at")
        serializer = CommandSerializer(command, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommandSubmitApiView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = CommandSerializer(data=request.data)
        if serializer.is_valid():
            command = Command.objects.create(
                items_needed=serializer.data["items_needed"]
            )
            success = command.prepare()

            if success:
                return Response(
                    command.get_information(), status=status.HTTP_201_CREATED
                )
        return Response(
            "The request is wrongly made", status=status.HTTP_400_BAD_REQUEST
        )


class CommandDetailApiView(APIView):

    def get_object(self, command_id):
        try:
            return Command.objects.get(identifier=command_id)
        except Command.DoesNotExist:
            return None
        except ValidationError:
            return None

    def get(self, request, command_id, *args, **kwargs):
        command_instance = self.get_object(command_id)
        if not command_instance:
            return Response(
                {"res": "Object with command id does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = CommandSerializer(command_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
