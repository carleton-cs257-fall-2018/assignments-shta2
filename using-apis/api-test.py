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
   url = base_url.format(coin, reference)
   req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
   data_from_server = urllib.request.urlopen(req).read()
   string_from_server = data_from_server.decode('utf-8')
   if ("Undefined property" in string_from_server):
      raise Exception("Unrecognised coin or currency. Please use 3-letter ticker symbol.")
   data = json.loads(string_from_server)
   
   response = "The current price of {0} in {1} is {2}".format(coin, reference, data['result'])
   return response
   
def get_change(coin):
    '''
    Returns the change of the requested coin in USD, in the past
    hour and in the past day.

    @param coin: requested coin to get change from
    '''
    base_url = 'https://chasing-coins.com/api/v1/std/coin/{0}'
    url = base_url.format(coin)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data_from_server = urllib.request.urlopen(req).read()
    string_from_server = data_from_server.decode('utf-8')
    change = json.loads(string_from_server)
    result = 'Change in {0} price in the past hour (USD): {1}. Change in {0} price in the past day (USD) {2}. '.format(coin, change['change']['hour'], change['change']['day'])


    return result

def main(args):
   if args.reference != None: 
      if args.action == 'change':
         raise Exception('Reference currency cannot be changed when evaluating change.')
      else:
         print(get_price(args.coin, reference=args.reference))
   elif args.action == 'change':
      print(get_change(args.coin))
   else:
     print(get_price(args.coin))
  
if __name__ == '__main__':
   parser = argparse.ArgumentParser()

   parser.add_argument('coin', help='the 3-letter ticker symbol of the coin you want to lookup')

   parser.add_argument('action',
                       metavar='action',
                       help='the information you would like on the coin ("price" or "change")',
                       choices=["price", "change"])

   parser.add_argument('--reference', type=str,
                        help='the currency you want to use as a reference when looking up price',
                        required = False)

   args = parser.parse_args()
    
    
   #if sys.argv.length not in [3, 4] or sys.argv[2] not in ["price", "change"]:
      
   main(args)