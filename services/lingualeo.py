# -*- coding: utf-8 -*-
import urlparse

import requests


requests_sesion = requests.Session()


class LinguaLeo(object):
    def __init__(self, email, password, base_api_url='https://api.lingualeo.com/api'):
        self.email = email
        self.password = password
        self.base_api_url = base_api_url

    def auth(self):
        data = {
            'email': self.email,
            'password': self.password
        }
        return self._make_post_request('login', data).json()

    def add_word(self, word, translated_word, context):
        data = {
            'word': word,
            'translated_word': translated_word,
            'context': context,
        }
        return self._make_post_request('addword', data).json()

    def get_translate(self, word):
        result = self._make_get_request('gettranslates', params={'word': word}).json()
        translate = result['translate'][0]
        return {
            'is_exist': translate['is_user'],
            'word': word,
            'translated_word': translate['value'],
        }

    def _make_post_request(self, resource, data):
        response = requests_sesion.post(urlparse.urljoin(self.base_api_url, resource), data=data)
        response.raise_for_status()
        return response

    def _make_get_request(self, resource, params):
        response = requests_sesion.get(urlparse.urljoin(self.base_api_url, resource), params=params)
        response.raise_for_status()
        return response
