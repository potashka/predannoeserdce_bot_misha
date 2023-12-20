import logging
from django.contrib import admin
from django.shortcuts import render
from django.urls import path

from app.forms import MessagesForm
from app.models import Customer, FAQ, Messages
from core.constants import EMPTY_FIELD_VALUE
from app.regular_messages import send_messages, start_scheduler, stop_scheduler

logger = logging.getLogger(__name__)


class FAQAdmin(admin.ModelAdmin):
    """Админка для часто задаваемых вопросов."""
    empty_value_display = EMPTY_FIELD_VALUE
    list_display = ('pk', 'question', 'order',)
    search_fields = ('question', 'answer',)


class CustomerAdmin(admin.ModelAdmin):
    """Админка для клиентов."""
    empty_value_display = EMPTY_FIELD_VALUE
    list_display = ('pk', 'name', 'email', 'tg_id', 'phone')
    search_fields = ('name', 'tg_id')


class MessagesAdmin(admin.ModelAdmin):
    """
    Админка для сообщений: админ может добавить текстовое сообщение
    дополнительно к рассылаемым random сообщениям из regular_messages.
    Например: Привет от Фуражкина!!!
    """
    list_display = ['text']
    form = MessagesForm
    actions = [
        'send_messages_view',
        'start_scheduler',
        'stop_scheduler'
    ]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'send_messages/', self.send_messages_view, name='send_messages'
            ),
            path(
                'start_scheduler/', self.start_scheduler,
                name='start_scheduler'
            ),
            path(
                'stop_scheduler/', self.stop_scheduler, name='stop_scheduler'
                ),
        ]
        return custom_urls + urls

    def send_messages_view(self, request, queryset=None):
        """Отправка одного сообщения"""
        selected_messages = list(queryset) if queryset else None
        try:
            send_messages(selected_messages)
            self.message_user(
                request,
                'Сообщения успешно отправлены подписчикам.'
            )
        except Exception as e:
            logger.error(f"Ошибка отправки сообщений: {e}")
            self.message_user(
                request,
                'Произошла ошибка при отправке сообщений.'
            )
        return render(request, 'admin/send_messages_done.html')
    send_messages_view.short_description = "Отправить сообщения"

    def start_scheduler(self, request, queryset=None):
        """Планировщик заданий - рассылка регулярных сообщений"""
        try:
            start_scheduler()
            self.message_user(request, 'Планировщик успешно запущен.')
        except Exception as e:
            logger.error(f"Ошибка при запуске планировщика: {e}")
            self.message_user(
                request,
                'Ошибка при запуске планировщика.'
            )
        return render(request, 'admin/start_scheduler_done.html')
    start_scheduler.short_description = "Запустить планировщик"

    def stop_scheduler(self, request, queryset=None):
        """Планировщик заданий - остановка рассылки регулярных сообщений"""
        try:
            stop_scheduler()
            self.message_user(request, 'Планировщик успешно остановлен.')
        except Exception as e:
            logger.error(f"Ошибка при остановке планировщика: {e}")
            self.message_user(
                request,
                'Ошибка при остановке планировщика.'
            )
        return render(request, 'admin/stop_scheduler_done.html')
    stop_scheduler.short_description = "Остановить планировщик"


admin.site.register(FAQ, FAQAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Messages, MessagesAdmin)
