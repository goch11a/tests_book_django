from rest_framework.test import APIClient, RequestsClient, APIRequestFactory, force_authenticate
from django.urls import reverse
from rest_framework import status
from .views import AuthorViewset
from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class AuthorTest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_author_list(self):
        response = self.client.get(reverse("author-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_anuthor(self):
        response = self.client.post(reverse("author-list"), {'name':'zaza', 'natinolity':'german'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_wrongauthor(self):
        response = self.client.post(reverse("author-list"), {'natinolity':'german'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class BookTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test_user', password='password123')
        self.token = RefreshToken.for_user(self.user)

    def test_book_list_anauth(self):
        response = self.client.post(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_book_list_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION= f'Bearer {self.token.access_token}')
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BookTestRequsetClient(TestCase):
    def setUp(self):
        self.client = RequestsClient()
        self.user = User.objects.create_user(username='test_user', password='password123')
        self.token = RefreshToken.for_user(self.user)
        self.client.headers.update({'Authorization': f'Bearer {self.token.access_token}'})
        

    def test_book_list(self):
        response = self.client.get('http://127.0.0.1:8000/api/books/')
        self.assertEqual(response.status_code, 200)


class AuthorCreateFactory(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='test_user', email='test_user@gmail.com', password='password123')

    def test_create_author_list_factory(self):
        request = self.factory.post('/authors/', {'name':'trawa', 'natinolity':'gudamakari'}, format='json')
        force_authenticate(request, user=self.user)
        response = AuthorViewset.as_view()(request)
        self.assertEqual(response.status_code, 201)