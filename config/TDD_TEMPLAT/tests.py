from django.test import TestCase
from django.urls import reverse


class TestPaginaInicial(TestCase):
    def test_RenderHtml(self):

        response = self.client.get(reverse('myview'))
        
        self.assertEqual(response.status_code, 200)
        
        self.assertContains(response, 'BEM VINDO A PAGINA')
 