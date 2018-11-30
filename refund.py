import argparse, os, csv, requests
from types import SimpleNamespace
from uuid import uuid1
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
url = 'https://www.google-analytics.com/collect'

def prepare_payload(transaction_id, product_sku, product_qty):
    payload = {
        'v': 1,
        't': 'event',
        'ni': 1,
        'cid': str(uuid1()),
        'tid': os.getenv('PROPERTY'),
        'dh': os.getenv('HOSTNAME'),
        'cd2': os.getenv('GTM'),
        'ec': os.getenv('EVENT_CATEGORY'),
        'ea': os.getenv('EVENT_ACTION'),
        'el': os.getenv('EVENT_LABEL'),
        'pa': 'refund',
        'ti': transaction_id,
        'pr1id': product_sku,
        'pr1qt': int(product_qty),
    }

    return payload

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process GA refund data.')
    parser.add_argument('-f', required=True, dest='filename', help='Name of the csv file to be processed.')
    parser.add_argument('-n', required=False, dest='dryrun', action='store_true', help='Dry Run.')
    parser.add_argument('-d', required=False, dest='debug', action='store_true', help='Debug.')
    args = parser.parse_args()

    with open(args.filename) as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }

        for row in reader:
            payload = prepare_payload(*row)
            if (args.debug):
                pprint(payload)

            a = SimpleNamespace(status_code = 200, headers=[])
            if (not args.dryrun):
                a = requests.post(url, data=payload, headers=headers)

            print('Sent refund to %s: transaction %s, SKU %s, quantity %s - status: %s' % (os.getenv('PROPERTY'), *row, a.status_code))
