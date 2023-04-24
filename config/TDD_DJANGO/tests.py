from django.test import TestCase
from models import User

# Create your tests here


class djangoTdd(TestCase):
    def test_novo_usuario(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.assertEqual(user.username, 'testuser')
