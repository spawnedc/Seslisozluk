#!/usr/bin/env python
import sys, urllib2
from bs4 import BeautifulSoup

def parse_response(word):

    response = urllib2.urlopen('http://m.seslisozluk.net/?word=%s' % word)
    html = response.read()

    soup = BeautifulSoup(html)

    results = soup.findAll('div', {'class': 'resultset'})

    for result in results:
        title = result.find('div', {'class': 'top'})
        translation = result.find('tbody')
        print title.text.strip()
        print translation.text
        print '\n'

if __name__ == "__main__":
    try:
        word = sys.argv[1]
    except IndexError:
        sys.exit('usage: %s word' % sys.argv[0])
    else:
        parse_response(word)