from rest_framework import serializers

from telegram_messages.models import Message


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Message
        fields = ['user', 'message', 'created_date']
