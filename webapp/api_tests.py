'''
    api_test
    Paul Butterfield and Conor Gormally
    10/15/18

    Unit tests for api responses
'''

import unittest, sys, json, urllib.request

class api_tests(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://perlman.mathcs.carleton.edu:5105"

    def tearDown(self):
        pass

    def get_data(url_endpoint):
        url = base_url + url_endpoint
        data_from_server = urllib.request.urlopen(url).read()
        string_from_server = data_from_server.decode('utf-8')
        data = json.loads(string_from_server)
        return data

    def test_candidate_by_name():
        pass

    def test_candidate_by_party():
        pass

    def test_candidate_by_state():
        pass

    def test_candidate_by_seat():
        pass

    def test_pac_by_name():
        pass

    def test_pac_by_party():
        pass

    def test_pac_by_industry():
        pass

    def test_pac_by_sensitive():
        pass

    def test_pac_by_foreign():
        pass

    def test_transactions_to_candidate():
        pass

    def test_transactions_to_pac():
        pass

    def test_transactions_indiv_to_pac():
        pass

    def test_invalid_candidate_name():
        pass

    def test_invalid_pac_name():
        pass

    def test_foreign_pacs_to_candidate():
        pass

    def test_transactions_indiv_to_candidate_by_state():
        pass
