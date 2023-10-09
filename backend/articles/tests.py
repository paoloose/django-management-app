"""
Article CRUD operations and authentication testing.

Note that TEST_REQUEST_DEFAULT_FORMAT is set to 'json' by default.
"""
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from articles.models import Article

class ArticleTest(APITestCase):
    def setUp(self):
        """
        Creates a new User and authenticates it.
        """
        credentials = {
            'username': 'tester_articles_test',
            'password': 'pass'
        }
        self.user = User.objects.create_user(**credentials, id=1)
        response = self.client.post(
            reverse('token-obtain-pair'),
            data=credentials
        )
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def unauthenticate(self):
        """
        Clears the authentication credentials (JWT).
        """
        self.client.credentials()

    def test_view_articles(self):
        """
        Both authenticated and unauthenticated users should be able to view.
        """
        article_list_url = reverse('article-list')

        response = self.client.get(article_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.unauthenticate()

        response = self.client.get(article_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_article(self):
        """
        Only authenticated users should be able to create a new article.
        This also checks if the article was created.
        """
        response = self.client.post(reverse('article-list'), {
            'title': 'Test Article',
            'content': 'Test Content',
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(Article.objects.get().title, 'Test Article')

        self.unauthenticate()

        response = self.client.post(reverse('article-list'), {
            'title': 'Test Article',
            'content': 'Test Content',
        })
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_article(self):
        """
        Only authenticated users should be able to delete an article.
        This also checks if the article was deleted successfully.
        """
        article = Article.objects.create(
            title='Test Article',
            content='Test Content'
        )
        article.save()
        self.assertEqual(Article.objects.count(), 1)

        response = self.client.delete(reverse('article-detail', args=[article.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Article.objects.count(), 0)

        # Deleting an article that doesn't exist should return 404
        response = self.client.delete(reverse('article-detail', args=[article.id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # And unauthorized users should not be able to delete an article
        self.unauthenticate()

        response = self.client.delete(reverse('article-detail', args=[article.id]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_article(self):
        """
        Only authenticated users should be able to update an article.
        This also checks if the article was updated successfully.
        """
        article = Article.objects.create(
            title='Test Article',
            content='Test Content'
        )
        article.save()
        self.assertEqual(Article.objects.count(), 1)

        response = self.client.put(reverse('article-detail', args=[article.id]), {
            'title': 'Updated Article',
            'content': 'Updated Content'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(Article.objects.get().title, 'Updated Article')

        # Updating an article that doesn't exist should return 404
        response = self.client.put(reverse('article-detail', args=[article.id + 1]), {
            'title': 'Updated Article',
            'content': 'Updated Content'
        })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # And unauthorized users should not be able to update an article
        self.unauthenticate()

        response = self.client.put(reverse('article-detail', args=[article.id]), {
            'title': 'Updated Article',
            'content': 'Updated Content'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
