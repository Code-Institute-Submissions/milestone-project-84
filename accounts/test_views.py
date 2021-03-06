from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.contrib import messages
from accounts.views import registration, login


class TestIndexviews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")


class TestRegistrationViewLoggedOut(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_page(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)


class TestRegistratationViewLoggedIn(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='person',
            email='fake@email.com',
            password='Jksdjfskdf1321@_password',
        )

    def test_register_page_redirect_to_home_when_logged_in(self):
        request = self.factory.get('/')
        request.user = self.user
        page = registration(request)
        self.assertEqual(page.status_code, 302)
        self.assertEqual(page.url, "/")


class LoginViewLoggedOut(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)


class TestLoginViewLoggedIn(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='person',
            email='fake@email.com',
            password='Jksdjfskdf1321@_password',
        )

    def test_login_form_successfully_submitted(self):
        user = User.objects.get(pk=1)
        self.assertEqual(user.username, "person")
        self.assertRaisesMessage(
            messages.success,
            "You have successfully logged in!")

    def test_login_page_redirect_to_home_when_logged_in(self):
        request = self.factory.get('/')
        request.user = self.user
        page = login(request)
        self.assertEqual(page.status_code, 302)
        self.assertEqual(page.url, "/")


class TestLogoutSuccesful(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='person',
            email='fake@email.com',
            password='Jksdjfskdf1321@_password',
        )
        self.client.login(
            username='person',
            password='test12345@_password')

    def test_logout_page_redirects_to_index(self):
        page = self.client.get("/accounts/logout/")
        self.assertEqual(page.status_code, 302)
        self.assertRaisesMessage(
            messages.success,
            "You have successfully been logged out!")
