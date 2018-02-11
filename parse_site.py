import sys
from urllib.parse import urlsplit
import json
from unidecode import unidecode

from recipe_parser import *

if __name__ == '__main__':

    if len(sys.argv) < 2:
        raise ValueError('No URL given')

    url = sys.argv[1]
    netloc = urlsplit(url).netloc
    
    if netloc in site_urls:
        parser = site_urls[netloc](url)
    else:
        raise ValueError('netloc %s not understood' % netloc)

    data = parser.compose()
    #print(json.dumps(data))
    print(data['title'])
    
    procedure = ""
    for x in data['directions']:
        procedure += x+'<br><br>'

    if len(data['notes']) > 0:
        procedure += "Notes:<br><br>"
        for x in data['notes']:
            procedure += x+'<br><br>'

    print(unidecode(procedure[:-8]))

    print(data['ingredients'])
    print(data['time'])
