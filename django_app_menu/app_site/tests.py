from django.test import TestCase
from django.db import connection


class TestSomething(TestCase):

    def test_something(self):
        counter = len(connection.queries)
        something()
        self.assertEquals(len(connection.queries), counter)
