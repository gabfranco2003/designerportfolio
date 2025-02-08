from django.test import TestCase

# Create your tests here.
class TestIndexView(TestCase):
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/index.html')
        self.assertContains(response, 'Welcome to my website!')
        self.assertContains(response, 'About Me')
        self.assertContains(response, 'Skills')
        self.assertContains(response, 'Education')
        self.assertContains(response, 'Experience')
        self.assertContains(response, 'Projects')
        self.assertContains(response, 'Contact Information')
        self.assertQuerysetEqual(response.context['skills'], [])
        self.assertQuerysetEqual(response.context['education'], [])
        self.assertQuerysetEqual(response.context['experience'], [])
        self.assertQuerysetEqual(response.context['projects'], [])
        self.assertIsNone(response.context['about_me'])
        self.assertIsNone(response.context['contact_info'])