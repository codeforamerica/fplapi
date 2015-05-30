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

    def test_content_type_json(self):
        response = self.app.get('/api?year=2014&size=3')
        self.assertEqual(response.content_type, 'application/json')

    def test_valid_fpl_percentage(self):
        response = self.app.get('/api?year=2014&size=3&income=20000')
        response = json.loads(response.data)
        self.assertEqual(response['fpl_percentage'], 101.06)

    def test_defaults_to_householdsize1_and_current_year(self):
        explicit_argument_response = self.app.get('/api?year=2015&size=1')
        no_argument_response = self.app.get('/api')
        self.assertEqual(explicit_argument_response.data, no_argument_response.data)
        only_size_arg_response = self.app.get('/api?size=1')
        self.assertEqual(explicit_argument_response.data, only_size_arg_response.data)
        only_year_arg_response = self.app.get('/api?year=2015')
        self.assertEqual(explicit_argument_response.data, only_year_arg_response.data)

if __name__ == '__main__':
      unittest.main()
