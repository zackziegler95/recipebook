import sys
from urllib.parse import urlsplit

from  recipe_parser import *

if __name__ == '__main__':

    if len(sys.argv) < 2:
        raise ValueError('No URL given')

    url = sys.argv[1]
    netloc = urlsplit(url).netloc
    
    if netloc in site_urls:
        parser = site_urls[netloc](url)
    else:
        raise ValueError('netloc %s not understood' % netloc)

    print(parser.compose())

