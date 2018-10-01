#!/usr/bin/env python3
'''
    api-test.py
    Paul Butterfield, Henry Pearson, 30 September 2018

    Retrieves data on cryptocurrencies from the https://chasing-coins.com 
    API and parses the results.
    
'''

import sys
import argparse
import json
import urllib.request

def get_price(coin, *, reference='USD'):
   '''
   Returns the price of the requested coin in USD unless a 
   different reference currency is specified using the 
   "reference" parameter.
   
   Throws exceptions on server errors and unrecognized coins
   or currencies.
   '''
   base_url = "https://chasing-coins.com/api/v1/convert/{0}/{1}"
   url = base_url.format(coin, reeference)
   data_from_server = urllib.request.urlopen(url).read()
   string_from_server = data_from_server.decode('utf-8')
   if ("Undefined property" in string_from_server):
      raise Exception("Unrecognised coin or currency. Please use 3-letter ticker symbol.")
   data = json.loads(string_from_server)
   
   return data['result']
   

   
  
if __name__ == '__main__':
   parser = argparse.ArgumentParser(description='Get word info from the Ultralingua API')

   parser.add_argument('coin', help='the 3-letter ticker symbol of the coin you want to lookup')

   parser.add_argument('action',
                       metavar='action',
                       help='the information you would like on the coin ("price" or "change")'
                       choices=["price", "change"])

   parser.add_argument('reference', 
                        help='the currency you want to use as a reference when looking up price',
                        required = False)

   args = parser.parse_args()
    
    
   #if sys.argv.length not in [3, 4] or sys.argv[2] not in ["price", "change"]:
      
   main(args)