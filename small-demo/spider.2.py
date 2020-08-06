from urllib import request
from io import BytesIO
import gzip
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class Spilder():

    url='https://www.douyu.com/g_LOL'

    def __fetch_content(self):
        r = request.urlopen(Spilder.url)
        htmls = r.read()
        buff = BytesIO(htmls)
        f = gzip.GzipFile(fileobj=buff)
        htmls = f.read().decode('utf-8')
        print(htmls)

    def go(self):
        self.__fetch_content()

spilder=Spilder()
spilder.go()