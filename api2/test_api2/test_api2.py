from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app



class TestBase(TestCase):
    def create_app(self):
        return app

class TestConsole(TestBase):
    def test_portugal(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('get_place'))
            self.assertIn(b'portugal', response.data)

    def test_spain(self):
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('get_place'))
            self.assertIn(b'spain', response.data)

    def test_america(self):
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for('get_place'))
            self.assertIn(b'america', response.data)


    def test_italy(self):
        with patch('random.randint') as r:
            r.return_value = 3
            response = self.client.get(url_for('get_place'))
            self.assertIn(b'italy', response.data)