import urllib2, re
from django.http import HttpResponse
from bs4 import BeautifulSoup
from django.utils import simplejson


def parse_response(self, word):

    url = 'http://m.seslisozluk.net/?word=%s' % word
    response = urllib2.urlopen(url)

    soup = BeautifulSoup(response.read(), from_encoding='utf-8')

    results = soup.findAll('div', {'class': 'resultset'})

    translations = []
    pattern = r'\d{1,3}\.\s([\w\s!,;()\X]+)+'

    for result in results:
        title = result.find('div', { 'class': 'top' })
        translation = result.find('tbody')
        matches = re.findall(pattern, unicode(translation.text), re.UNICODE)

        if matches:
            translations.append({
                'title': title.text,
                'translations': matches
            })
    print response.headers['content-type']

    return HttpResponse(simplejson.dumps(translations), content_type="application/json")