from http import HTTPStatus
from django.test import Client, TestCase
from django.core.cache import cache


class StaticPagesURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_about_url_exists_at_desired_location(self):
        """Проверка доступности страниц."""
        cache.clear()
        response = self.guest_client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK.value)
        
        cache.clear()
        response = self.guest_client.get("/second_page/")
        self.assertEqual(response.status_code, HTTPStatus.OK.value)

    def test_page_shows_correct_content(self):
        """Проверка контента страниц."""
        cache.clear()
        response = self.guest_client.get("/")
        self.assertContains(response, "У меня получилось!")
        
        cache.clear()
        response = self.guest_client.get("/second_page/")
        self.assertContains(response, "А это вторая страница!")
