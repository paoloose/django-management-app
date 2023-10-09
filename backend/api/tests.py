"""
Article CRUD operations and authentication testing.

Note that TEST_REQUEST_DEFAULT_FORMAT is set to 'json' by default.
"""
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class ArticleTest(APITestCase):
    def test_jwt_auth(self):
        """
        Basic JWT transactions: token obtain, token refresh, token verify.
        Further tests should be done in upstream.

        Authentication is done by username and password.
        """
        credentials = {
            'username': 'tester_api_test',
            'password': 'pass'
        }
        user = User.objects.create_user(**credentials)
        user.save()

        response = self.client.post(
            reverse('token-obtain-pair'),
            data=credentials
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data and 'refresh' in response.data)
        refresh_token = response.data['refresh']

        # Test token refresh
        response = self.client.post(
            reverse('token-refresh'),
            data={'refresh': 'this is an invalid token'}
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.post(
            reverse('token-refresh'),
            data={'refresh': refresh_token}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
