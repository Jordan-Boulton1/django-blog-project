from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm

class TestAboutView(TestCase):


    def setUp(self):
        self.about_me = About(
            title="About me", content="This is about me")
        self.about_content.save()

    def test_render_about_page_with_collaborate_form(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About me', response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)