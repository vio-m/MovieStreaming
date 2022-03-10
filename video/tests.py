from django.test import SimpleTestCase, TransactionTestCase
from django.urls import reverse, resolve
from .models import Video
from .views import all, detail, search, genres


class TestUrls(SimpleTestCase):

    def test_all(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, all)

    def test_detail(self):
        url = reverse('movie', args=[1])
        self.assertEquals(resolve(url).func, detail)

    def test_search(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, search)

    def test_genres(self):
        url = reverse('genres', args=[3])
        self.assertEquals(resolve(url).func, genres)


class TestViews(TransactionTestCase):

    def setUp(self):
        self.new_entry = Video.objects.create(title='test', year=1984, rating=5.0)

    def test_search(self):
        qs = Video.objects.get(title__icontains='test')
        self.assertEquals(qs, self.new_entry)




