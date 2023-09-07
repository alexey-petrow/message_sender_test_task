from rest_framework import status
from rest_framework.exceptions import APIException

# ----- regular exceptions: -----


class MessageException(Exception):
    pass


class UserEmptyTokenException(MessageException):
    pass


class ChatIdNodFoundException(MessageException):
    pass


# ----- api exceptions: -----


class GetUserChatIdApiException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Error when getting user chat_id.'
