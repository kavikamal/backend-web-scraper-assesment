"""
Use the argparse library to parse a URL passed in as a command line argument.
Use the requests library to retrieve the text of the
webpage at the specified URL.
Use the re library to look for email addresses, URLs,
and phone numbers included in the page.
"""

import sys
import argparse
import requests
import re


def requestUrl(req_url):
    r = requests.get(req_url)
    emails = list(set(re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+"
                                 r"\.[a-zA-Z0-9-.]+)", r.content)))
    print "Emails:"
    for email in emails:
        print email
    urls = list(set(re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-&(-_@.&+]|"
                    r"[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", r.content)))
    print "URLs:"
    for url in urls:
        print url
    # This regex pater will find a phone number
    # with any special char connecting numbers
    # phones = re.findall(r'1?\W*([2-9][0-8][0-9]\W*[2-9][0-9]{2}\W*[0-9]{4})',
    # r.content)
    phones = list(set(re.findall(r'1?\W*([2-9][0-8][0-9]\-[2-9][0-9]{2}\-'
                                 r'[0-9]{4})', r.content)))
    print "Phone Numbers:"
    for phone in phones:
        print phone


def main(args):
    if not args:
        sys.exit(1)
    parser = argparse.ArgumentParser(description='Process a url.')
    parser.add_argument('url', help='URL to scrape')
    args = parser.parse_args()
    # print args.url
    requestUrl(args.url)


if __name__ == '__main__':
    main(sys.argv[1:])
