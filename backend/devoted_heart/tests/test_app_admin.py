from django.test import TestCase
from app.admin import FAQAdmin, CustomerAdmin, MessagesAdmin
from app.models import FAQ, Customer, Messages
from django.contrib.auth import get_user_model
from django.urls import reverse


class FAQAdminTest(TestCase):

    def test_list_display(self):
        faq_admin = FAQAdmin(FAQ, None)
        self.assertEqual(
            faq_admin.list_display,
            ('pk', 'question', 'answer', 'category', 'order')
        )


class CustomerAdminTest(TestCase):

    def test_list_display(self):
        customer_admin = CustomerAdmin(Customer, None)
        self.assertEqual(
            customer_admin.list_display,
            ('pk', 'name', 'email', 'tg_id', 'phone', 'registration_date')
        )


class MessagesAdminTest(TestCase):

    def test_list_display(self):
        messages_admin = MessagesAdmin(Messages, None)
        self.assertEqual(
            messages_admin.list_display,
            ('text', 'image', 'selected')
        )

    def setUp(self):
        User = get_user_model()  # в тесте ушли от модели юзерс
        self.user = User.objects.create_user(
            username='admin', password='admin123', is_staff=True
        )
        self.message = Messages.objects.create(
            text='Test Message', image=None, selected=False
        )

    def test_send_messages_view(self):
        self.client.login(username='admin', password='admin123')

        url = reverse('admin:send_messages')
        data = {
            'action': 'send_messages_view',
            '_selected_action': [str(self.message.id)]
        }

        response = self.client.post(url, data, follow=True)

        self.assertEqual(response.status_code, 200)

        self.assertIn(
            'Сообщения успешно отправлены подписчикам.'.encode('utf-8'),
            response.content
        )

    def test_start_scheduler(self):
        self.client.login(username='admin', password='admin123')

        url = reverse('admin:start_scheduler')
        data = {
            'action': 'start_scheduler',
            '_selected_action': [str(self.message.id)]
        }

        response = self.client.post(url, data, follow=True)

        self.assertEqual(response.status_code, 200)

        self.assertIn(
            'Планировщик успешно запущен.'.encode('utf-8'), response.content
        )

    def test_stop_scheduler(self):
        self.client.login(username='admin', password='admin123')

        url = reverse('admin:stop_scheduler')
        data = {
            'action': 'stop_scheduler',
            '_selected_action': [str(self.message.id)]
        }

        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)

        self.assertIn(
            'Планировщик успешно остановлен.'.encode('utf-8'), response.content
        )
