from http import HTTPStatus
from django.test import Client, TestCase


class StaticPagesURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_about_url_exists_at_desired_location(self):
        """Проверка доступности страниц."""
        response = self.guest_client.get("/")
        self.assertEqual(response, HTTPStatus.OK)

        response = self.guest_client.get("/second_page/")
        self.assertEqual(response, HTTPStatus.OK)

    def test_page_shows_correct_content(self):
        """Проверка контента страниц."""
        response = self.guest_client.get("/")
        self.assertContains(response.text, "У меня получилось!")

        response = self.guest_client.get("/second_page/")
        self.assertContains(response.text, "А это вторая страница!")
