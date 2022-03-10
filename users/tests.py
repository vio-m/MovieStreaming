from django.test import TestCase
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse


User = get_user_model()


class TestUser(TestCase):

    def setUp(self):
        test_user = User(username='test', email='test@email.com')
        pw = '12pass34word56TEST'
        self.pw = pw
        test_user.is_superuser = True
        test_user.is_staff = True
        test_user.set_password(pw)
        test_user.save()
        self.test_user = test_user
        self.login_url = reverse('login')
        #User.objects.create_user(self.test_user)

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    def test_user_password(self):
        test_user = User.objects.get(username='test')
        self.assertTrue(test_user.check_password(self.pw))

    def test_login_url(self):
        self.assertEqual(settings.LOGIN_URL, self.login_url)

    def test_login(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_redirect(self):
        data = {"username": self.test_user, "password": self.pw}
        response = self.client.post(settings.LOGIN_URL, data, follow=True)
        redirect_path = response.request.get("PATH_INFO")
        self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)
        #or:
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL, status_code=302,
                             target_status_code=200, fetch_redirect_response=True)


















