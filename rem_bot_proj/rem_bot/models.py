from django.db import models

class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='ID пользователя',
        unique=True
    )
    name = models.TextField(
        verbose_name='Имя пользователя'
    )
    username = models.TextField(
        verbose_name='Никнейм'
    )
    count = models.TextField(
        verbose_name='Количество запросов'
    )

    def __str__(self):
        return f'#{self.external_id} {self.name} {self.username}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class Stat(models.Model):
    date = models.TextField(
        verbose_name='Дата',
        unique=True
    )
    count = models.PositiveIntegerField(
        verbose_name='Кол-во'
    )

    def __str__(self):
        return f'#{self.date} {self.count}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'