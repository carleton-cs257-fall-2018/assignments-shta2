'''
    api_test
    Paul Butterfield and Conor Gormally
    10/15/18

    Unit tests for api responses
'''

import unittest, sys, json, urllib.request

class api_tests(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://perlman.mathcs.carleton.edu:5105/"

    def tearDown(self):
        pass

    def get_data(url_endpoint):
        self.url = self.base_url + url_endpoint
        self.data_from_server = urllib.request.urlopen(self.url).read()
        self.string_from_server = self.data_from_server.decode('utf-8')
        self.data = json.loads(self.string_from_server)
        return self.data



    def test_candidates_by_name():
        self.assertEquals(get_data('candidates?name=Doe'),
              [{'id':'Muleqvse5de', 'first_name':'John', 'last_name':'Doe', 'party':'D', 'state':'AK', 'seat':'S1'}])

    def test_candidates_by_party_by_state():
        self.assertEquals(get_data('candidates?state=VA&party=D'), get_data('candidates?name=Maddison'))

    def test_candidates_by_state_by_seat():
        self.assertEquals(get_data('candidates?state=VA&seat=17'), get_data('candidates?name=Johnson'))



    def test_pacs_by_name():
        self.assertEquals(get_data('pacs?name=Democratic+Republicans+for+a+New+America'),
                     [{'id':'wsvyhdul2', 'name':'Democratic Republicans for a New America', 'party':'L',
                     'industry':'Architectural services', 'sensitive':'true', 'foreign':'true'}])

    def test_pacs_by_party_sensitive():
        self.assertEquals(get_data('pacs?party=D&sensitive=true'), get_data('pacs?id=znkcdot2b'))

    def test_pacs_by_industry_by_foreign():
        self.assertEquals(get_data('pacs?industry=Oil+and+Gas&foreign=true'), get_data('pacs?id=h8bmw42by'))



    def test_transactions_to_candidate():
        self.assertEquals(get_data('trasactions/to_candidate/David'), [{'date': '2017-10-04', 'amount':'25',
                              'contribID': '4alarvf3qvlg', 'contribType': 'indiv', 'recipID': '7f5ozph2h', 'recipType': 'cand'}])

    def test_transactions_to_candidate_by_contribType():
        self.assertEquals(get_data('transactions/to_candidate/Maddison?contribType=indiv'), get_data('transactions?max_amount = 20&min_amount=0'))

    def test_transactions_from_pac():
        self.assertEquals(get_data('transactions/from_pac/Republicans+For+When+Democrats+Were+Republicans'),
                            get_data('transactions/from_pac?start_date=2017-11-26&end_date=2017-11-28'))

    def test_transactions_by_date_by_recipType():
        self.assertEquals(get_data('transactions?start_date=2017-10-03&end_date=2017-10-09&recipType=pac'),
                          get_data('transactions?max_amount=501&min_amount=499'))

    def test_transactions_by_amount():
        self.assertEquals(get_data('transactions?max_amount=0&min_amount=-400'), [{'date':'2018-06-05', 'amount': -350,
                                   'contribID': 'rm8gcnwothb9', 'contribType': 'indiv', 'recipID':'7f5ozph2h', 'recipType': 'cand'}] )


    def test_invalid_amount_type():
        self.assertEquals(get_data('transactions?max_amount=f+to+pay+respects'), 'Input Error: Min amount must be number')
