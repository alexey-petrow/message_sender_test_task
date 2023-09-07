from django.db import models

from users.models import CustomUser


class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField()
    created_date = models.DateTimeField('creation date', auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'Message of user {self.user}: {self.message[:20]}'
