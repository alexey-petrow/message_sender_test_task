from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from api.exceptions import MessageException, GetUserChatIdApiException
from api.pagination import MessagePagination
from api.serializers.message_serializers import MessageSerializer
from api.services import MessageSenderService
from config import container
from telegram_messages.models import Message
from users.models import CustomUser


class MessageView(ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MessagePagination

    def get_queryset(self):
        return Message.objects.select_related('user').filter(user=self.request.user)

    def perform_create(self, serializer):
        user: CustomUser = self.request.user
        user_token: str = user.telegram_token

        message_sender_service: MessageSenderService = container.message_sender_service()
        try:
            message_sender_service.get_user_chat_id(user_token)
        except MessageException as error:
            raise GetUserChatIdApiException(detail=error)

        serializer.save(user=self.request.user)

        message = self.request.data.get('message')
        message_sender_service.send_message(message)
