from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from api.pagination import MessagePagination
from api.serializers.message_serializers import MessageSerializer
from telegram_messages.models import Message


class MessageView(ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MessagePagination

    def get_queryset(self):
        return Message.objects.select_related('user').filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        # TODO: отправка сообщения боту
