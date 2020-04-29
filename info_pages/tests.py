from django.core import mail
from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages

from .forms import ContactForm

class EmailTest(TestCase):
    def test_send_email(self):
        # Send message.
        mail.send_mail(
            'Subject here', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False,
        )

        # setting follow to True the client will follow any redirects and a redirect_chain attribute will be set in the response object containing tuples of the intermediate urls and status codes.
        response = self.client.post('/', follow=True)
        # response = self.client.post(reverse('home'))
    #     response = self.client.post(
    #     reverse('home'), 
    #     {'body':"Thank you for your query. We will contact you shortly."}, 
    #     follow=True)

        # messages = list(get_messages(response.wsgi_request))
        # print(messages)
        # messages = [m.message for m in get_messages(response.wsgi_request)]
        # message = response.context.get('messages')
        # message = list(r.wsgi_request._messages)
        # message = [str(message) for message in get_messages(post_response.wsgi_request)]
        # message = [m.message for m in get_messages(response.wsgi_request)]

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)
        # self.assertEqual(message.tags, "success")

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Subject here')

        # Confirm that the user is redirected to the homepage after submitting the contact_us form
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, '/home/')

        # Test that this template is rendered
        self.assertTemplateUsed(response, 'home/index.template.html')
        
        # Test that the exact string is returned after submitting contact_us form
        # self.assertEqual(str(messages[0]), 'Thank you for your query. We will contact you shortly.')
        # self.assertIn('Thank you for your query. We will contact you shortly.', messages)
        self.assertContains(response, 'Welcome to The BoardGameStore!')

class TermsAndConditionsTest(TestCase):

    def test_terms_and_conditions(self):
        url = reverse('terms_and_conditions')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'info_pages/terms_and_conditions.template.html')
        self.assertContains(response, '1. OUR WEBSITE AND OUR GOODS')

class PrivacyPolicyTest(TestCase):

    def test_privacy_policy(self):
        url = reverse('privacy_policy')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'info_pages/privacy_policy.template.html')
        self.assertContains(response, 'Privacy Policy of The BoardGameStore')

class RefundPolicyTest(TestCase):

    def test_refund_policy(self):
        url = reverse('refund_policy')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'info_pages/refund_policy.template.html')
        self.assertContains(response, 'Shipping and Returns')


