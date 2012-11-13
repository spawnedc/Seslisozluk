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

    for result in results:
        title = result.find('div', { 'class': 'top' })
        translation = result.find('tbody')
        matches = []

        for i in xrange(1, len(translation.contents), 2):
            content = translation.contents[i]
            matches.append(content.strip())

        if matches:
            translations.append({
                'title': title.text.strip(),
                'translations': matches
            })

    return HttpResponse(simplejson.dumps(translations), content_type="application/json")