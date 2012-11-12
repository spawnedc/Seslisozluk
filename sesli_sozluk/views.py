import urllib2
from django.http import HttpResponse
from bs4 import BeautifulSoup
from django.utils import simplejson

def parse_response(self, word):

    url = 'http://m.seslisozluk.net/?word=%s' % word
    response = urllib2.urlopen(url)

    soup = BeautifulSoup(response.read())

    results = soup.findAll('div', {'class': 'resultset'})

    translations = []

    for result in results:
        title = result.find('div', { 'class': 'top' })
        translation = result.find('tbody')
        translations.append({
            'title': title.text,
            'content': translation.text
        })

    return HttpResponse(simplejson.dumps(translations), content_type="application/json")