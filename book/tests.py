from rest_framework.test import APIClient, RequestsClient, APIRequestFactory, force_authenticate
from django.urls import reverse
from rest_framework import status
from .views import AuthorViewset
from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Author, Book

import pytest

@pytest.mark.django_db
def test_author_book_realtionship():
    author = Author.objects.create(name='vaja', natinolity='georigian')
    
    
    Book.objects.create(title='love', author=author, publication_date='2021-02-03')
    Book.objects.create(title='gilty', author=author, publication_date='2022-12-02')
    
    assert Book.objects.filter(author=author).count() == 2

    author.delete()

    assert Book.objects.count() == 0

@pytest.mark.django_db
def test_book_creation():  
    author = Author.objects.create(name='noe', natinolity='georigian') 
    
    Book.objects.create(title='tolma', author=author, publication_date='2021-03-11') 
    client = APIClient()
    response = client.get('/api/books/')
    assert response.status_code == 401

    # client = APIClient()
    # url = '/api/books/'
    # response = client.post(url, {'title':'tolma', 'publication_date': '2021-03-11'}, format='json')

    # assert response.status_code == 401

@pytest.mark.django_db
def test_author_pagination():
    client = APIClient()

    for i in range(15):
        Author.objects.create(name=f'author{i}', natinolity=f'country{i}')

    response = client.get('/api/authors/')
    assert response.status_code == 200
    assert len(response.data['results']) == 10
    assert 'next' in response.data
    assert response.data['next'] is not None

@pytest.mark.django_db
def test_filter_authors():
    client = APIClient()
    url = '/api/authors/'

    Author.objects.create(name='noe', natinolity='libanian')
    Author.objects.create(name='gio', natinolity='georgian')
    Author.objects.create(name='lasha', natinolity='georgian')

    
    
    response = client.get(url, {'natinolity':'georgian'})
    authors = response.data['results']
    assert response.status_code == 200
    assert all(author['natinolity'] == 'georgian' for author in authors)
    # assert len(response.data['results']) == len(['georgian' for _ in authors])




# class AuthorTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
    
#     def test_author_list(self):
#         response = self.client.get(reverse("author-list"))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    
#     def test_create_anuthor(self):
#         response = self.client.post(reverse("author-list"), {'name':'zaza', 'natinolity':'german'}, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_create_wrongauthor(self):
#         response = self.client.post(reverse("author-list"), {'natinolity':'german'})
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# class BookTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(username='test_user', password='password123')
#         self.token = RefreshToken.for_user(self.user)

#     def test_book_list_anauth(self):
#         response = self.client.post(reverse('book-list'))
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

#     def test_book_list_auth(self):
#         self.client.credentials(HTTP_AUTHORIZATION= f'Bearer {self.token.access_token}')
#         response = self.client.get(reverse('book-list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class BookTestRequsetClient(TestCase):
#     def setUp(self):
#         self.client = RequestsClient()
#         self.user = User.objects.create_user(username='test_user', password='password123')
#         self.token = RefreshToken.for_user(self.user)
#         self.client.headers.update({'Authorization': f'Bearer {self.token.access_token}'})
        

#     def test_book_list(self):
#         response = self.client.get('http://127.0.0.1:8000/api/books/')
#         self.assertEqual(response.status_code, 200)


# class AuthorCreateFactory(TestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()
#         self.user = User.objects.create_user(username='test_user', email='test_user@gmail.com', password='password123')

#     def test_create_author_list_factory(self):
#         request = self.factory.post('/authors/', {'name':'trawa', 'natinolity':'gudamakari'}, format='json')
#         force_authenticate(request, user=self.user)
#         response = AuthorViewset.as_view()(request)
#         self.assertEqual(response.status_code, 201)