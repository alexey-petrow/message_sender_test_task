# Generated by Django 4.2.5 on 2023-09-05 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_first_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='token',
            new_name='telegram_token',
        ),
    ]
