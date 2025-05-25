# Existing model test
from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def test_create_post(self):
        post = Post.objects.create(title='Test Title', content='Test content')
        self.assertEqual(post.title, 'Test Title')
        self.assertEqual(post.content, 'Test content')
        self.assertIsNotNone(post.created_at)


# New API tests (paste below model test)
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class PostAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.post = Post.objects.create(title='Sample Post', content='Content of the post')

    def test_auth_required(self):
        unauthenticated_client = APIClient()
        response = unauthenticated_client.get('/api/posts/')
        self.assertEqual(response.status_code, 401)

    def test_get_posts(self):
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Sample Post')

    def test_create_post(self):
        data = {'title': 'New Post', 'content': 'New content'}
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, 201)

    def test_update_post(self):
        data = {'title': 'Updated', 'content': 'Updated content'}
        response = self.client.put(f'/api/posts/{self.post.id}/', data)
        self.assertEqual(response.status_code, 200)

    def test_delete_post(self):
        response = self.client.delete(f'/api/posts/{self.post.id}/')
        self.assertEqual(response.status_code, 204)
