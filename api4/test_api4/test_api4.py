from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_portugal_skiing(self):
        response = self.client.post(url_for('post_task'), data = 'portugal skiing')
        self.assertIn(b'go to ski at serra da estrela', response.data)

    def test_portugal_jetskiing(self):
        response = self.client.post(url_for('post_task'), data = 'portugal jetskiing')
        self.assertIn(b'jetskiing in lagos', response.data)

    def test_portugal_snowboarding(self):
        response = self.client.post(url_for('post_task'), data = 'portugal snowboarding')
        self.assertIn(b'snowbaord at the mountains near a town called Loriga', response.data)

    def test_portugal_kayaking(self):
        response = self.client.post(url_for('post_task'), data = 'portugal kayaking')
        self.assertIn(b'kayak and explore the algarve regions in portugal', response.data)

    def test_spain_skiing(self):
        response = self.client.post(url_for('post_task'), data = 'spain skiing')
        self.assertIn(b'ski on the mountains of sierra nevada', response.data)

    def test_spain_jetskiing(self):
        response = self.client.post(url_for('post_task'), data = 'spain jetskiing')
        self.assertIn(b'jetskiing in barcelona', response.data)

    def test_spain_snowboard(self):
        response = self.client.post(url_for('post_task'), data = 'spain snowboarding')
        self.assertIn(b'snowboard at the formigal resort', response.data)

    def test_spain_kayaking(self):
        response = self.client.post(url_for('post_task'), data = 'spain kayaking')
        self.assertIn(b'kayak on the guadalquivir River, Seville', response.data)

    def test_italy_skiing(self):
        response = self.client.post(url_for('post_task'), data = 'italy skiing')
        self.assertIn(b'ski at the mountains in dolomites', response.data)

    def test_italy_jetskiing(self):
        response = self.client.post(url_for('post_task'), data = 'italy jetskiing')
        self.assertIn(b'jetski at the marine reserves in italy', response.data)

    def test_italy_snowboard(self):
        response = self.client.post(url_for('post_task'), data = 'italy snowboarding')
        self.assertIn(b'snowboard in livigno in italy', response.data)

    def test_italy_kayaking(self):
        response = self.client.post(url_for('post_task'), data = 'italy kayaking')
        self.assertIn(b'kayak in venice', response.data)
    
    def test_america_skiing(self):
        response = self.client.post(url_for('post_task'), data = 'america skiing')
        self.assertIn(b'ski in aspen United States', response.data)

    def test_america_jetskiing(self):
        response = self.client.post(url_for('post_task'), data = 'america jetskiing')
        self.assertIn(b'jetski at the miami south beach', response.data)

    def test_america_snowboard(self):
        response = self.client.post(url_for('post_task'), data = 'america snowboarding')
        self.assertIn(b'snowboard at the park city in the utah olympic park', response.data)

    def test_america_kayaking(self):
        response = self.client.post(url_for('post_task'), data = 'america kayaking')
        self.assertIn(b'kayak at the juniper Run, Ocala National Forest', response.data)

    def test_else(self):
        response = self.client.post(url_for('post_task'), data = 'notspain notkayaking')
        self.assertIn(b'No Holiday could be generated', response.data)
    