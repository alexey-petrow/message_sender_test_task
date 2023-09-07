# message_sender_test_task
## Сервис доступен по адресу:
http://51.250.91.102

http://51.250.91.102/admin - админ зона
## Примеры api запросов:

### Регистрация нового пользователя:

- POST запрос на эндпоинт:
```
/api/v1/auth/users/
```
- в теле запроса(body):
```
{
    "username": "Sania",
    "first_name": "Sania",
    "password": "Saniaqwe123"
}
```
- ответ:
```
{
    "first_name": "Sania",
    "username": "Sania",
    "id": "8402d076-dad5-46c6-b297-e70de7e57b6d"
}
```

### Получение JWT токена для зарегистрированного пользователя:

- POST запрос на эндпоинт:
```
/api/v1/auth/jwt/create/
```
- в теле запроса(body):
```
{
    "username": "Sania",
    "password": "Saniaqwe123"
}
```
- ответ:
```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NjY3Mzc3NSwiaWF0IjoxNjk0MDgxNzc1LCJqdGkiOiJmNmM5YzNiMWE5MDQ0MzU3YjRkNzQ3NzUwOWQ4MjkwNyIsInVzZXJfaWQiOiIxNzBlNGQ1Yy1hMGFlLTQ5ZmItOWFkYS0xMzY5YjBiMzliMzMifQ.CB51fLai4ebUqmHKy5eJQqu54pmckFE2ZkikiXaynTM",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk0MTY4MTc1LCJpYXQiOjE2OTQwODE3NzUsImp0aSI6ImVmOTAzNzIzZGNjNzRkOTc5NjEwNWMwMmU2YjZjZjU2IiwidXNlcl9pZCI6IjE3MGU0ZDVjLWEwYWUtNDlmYi05YWRhLTEzNjliMGIzOWIzMyJ9.MwGWkNJa6mniXWOP6XKHFUSX4eobDoE71Jhh-Z1cdTQ"
}
```
- access **токен** передается в заголовке запроса для авторизации пользователя.
- Пример: 'Authorization: JWT eyJhbGciOiJIUzI1NiI...'
- Передача access токена необходима во всех последующих запросах

### Получение специального токена для отправки телеграм боту:

- GET запрос на эндпоинт (авторизированный запрос):
```
/api/v1/get_telegram_token/
```

- ответ:
```
{
    "telegram_token": "1849b5a8a02eba338bd8e8ccc8e29cef2ef677a70a7d0afe43897ccf8f0807cd",
    "send_token_to_telegram_bot": "@pilusha_bot"
}
```

- Полученный в примере токен нужно отправить телеграм боту @pilusha_bot через клиентское приложение

### Получение нового токена для отправки телеграм боту:
#### Необходимо если токен скомпрометирован.

- PATCH запрос на эндпоинт (авторизированный запрос):
```
/api/v1/refresh_telegram_token/
```

- ответ:
```
{
    "telegram_token": "2bebd068e7c799851f77a0e1fb3844848ac762aa5e4559b30b378ce22d1af378",
    "send_token_to_telegram_bot": "@pilusha_bot"
}
```

### Отправка сообщений:

- POST запрос на эндпоинт (авторизированный запрос):
```
/api/v1/message/
```
- в теле запроса(body):
```
{
    "message": "qwe123"
}
```
- ответ:
```
{
    "user": "Sania",
    "message": "qwe123",
    "created_date": "2023-09-07T22:15:35.484473Z"
}
```

### Получение всех сообщений пользователя:

- GET запрос на эндпоинт (авторизированный запрос):
- в параметре запроса можно передать номер страницы(page=1) и количество сообщений на страницу(page_size=2)
```
/api/v1/message/?page=1&page_size=2
```
- ответ:
```
{
    "count": 4,
    "next": "http://127.0.0.1/api/v1/message/?page=2&page_size=2",
    "previous": null,
    "results": [
        {
            "user": "Sania",
            "message": "ccc123",
            "created_date": "2023-09-07T22:18:07.793247Z"
        },
        {
            "user": "Sania",
            "message": "ccc123",
            "created_date": "2023-09-07T22:18:05.915687Z"
        }
    ]
}
```
