from django.test import TestCase
from django.contrib.auth import get_user_model
from user.forms import UserLoginForm, UserRegistrationForm, MyDetailsForm


class UserLoginFormTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="test1234",
            name="Test User"
        )

    def test_valid_form(self):
        """Test valid form"""
        form = UserLoginForm({
            "email": "test@gmail.com",
            "password": "test1234"
        })
        self.assertTrue(form.is_valid())

    def test_email_missing(self):
        """Test user submits invalid username"""
        form = UserLoginForm({
            "email": "",
            "password": "test1234"
        })
        # self.assertEqual(
        #     form.non_field_errors(), [
        #         form.errors['invalid_login'] % {
        #             'username': User._meta.get_field('username').verbose_name
        #         }
        #     ]
        #
        # )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'],  [u'This field is required.'])





















