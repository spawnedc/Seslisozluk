from google.appengine.api import urlfetch
from django.http import HttpResponse
from bs4 import BeautifulSoup
import simplejson

def parse_response(self, word):

    url = 'http://m.seslisozluk.net/?word=%s' % word
    response = urlfetch.fetch(url)

    soup = BeautifulSoup(response.content)

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