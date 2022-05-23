from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_getholiday(self):
        with patch("requests.get") as g:
            with patch("requests.post") as p:
                g.return_value.text = "portugal skiing"
                p.return_value.text = "go to ski at serra da estrela"
                response = self.client.get(url_for('get_holiday'))
                self.assertIn(b'portugal skiing', response.data)
                self.assertIn(b'go to ski at serra da estrela', response.data)
