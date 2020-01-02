# from django.http import HttpResponseNotFound, HttpResponseServerError
# from django.test import TestCase, Client
#
#
# class ErrorViewTests(TestCase):
#     """Test error handler views"""
#
#     def setUp(self):
#         self.client = Client()
#
#     def test_404_view(self):
#         """Test 404 error page"""
#         response = HttpResponseNotFound("fail")
#         self.assertEqual(response.status_code, 404)
#         self.assertTemplateUsed("404.html")
#
#     def test_500_view(self):
#         """Test 404 error page"""
#         response = HttpResponseServerError()
#         response_1 = self.client.get()
#         self.assertEqual(response.status_code, 500)
#         self.assertTemplateUsed("500.html")
