#!/usr/bin/env python
# -*- coding: utf8 -*-

import unittest
import json
from run import app

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_amount(self):
        response = self.app.get('/api?year=2014&size=3')
        response = json.loads(response.data)
        self.assertEqual(response['amount'], 19790)

if __name__ == '__main__':
      unittest.main()
