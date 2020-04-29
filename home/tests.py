from django.test import Client, TestCase

class HomePageTestCase(TestCase):

    def test_index(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.template.html')
        self.assertContains(response, 'Welcome to The BoardGameStore!')
        # self.assertEqual(len(response.context['homepage_display']), 8)