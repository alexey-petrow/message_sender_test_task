import secrets

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from users.models import CustomUser


def _generate_new_telegram_token_to_user(user: CustomUser) -> str:
    assert isinstance(user, CustomUser)
    token: str = secrets.token_hex(32)
    user.telegram_token = token
    user.save()
    return token


class TelegramTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        user: CustomUser = request.user
        token: str | None = user.telegram_token
        if not token:
            token: str = _generate_new_telegram_token_to_user(user)
        return Response(data={'telegram_token': token}, status=status.HTTP_200_OK)


class RefreshTelegramTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request: Request):
        user: CustomUser = request.user
        token: str = _generate_new_telegram_token_to_user(user)
        return Response(data={'telegram_token': token}, status=status.HTTP_200_OK)
