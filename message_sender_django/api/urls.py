from django.urls import path, include
from api.views.telegram_token_views import TelegramTokenView, RefreshTelegramTokenView

v1_urls = [
    path('get_telegram_token/', TelegramTokenView.as_view()),
    path('refresh_telegram_token/', RefreshTelegramTokenView.as_view()),
]

urlpatterns = [
    path('v1/', include(v1_urls)),
]
