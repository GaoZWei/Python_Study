from urllib import request
from io import BytesIO
import re
import gzip
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class Spilder():

    url='https://www.douyu.com/g_LOL'
    root_pattern='<div class="DyListCover-info">[\s\S]*?</div>'
    def __fetch_content(self):
        r = request.urlopen(Spilder.url)
        htmls = r.read()
        buff = BytesIO(htmls)
        f = gzip.GzipFile(fileobj=buff)
        htmls = f.read().decode('utf-8')
        # htmls = str(f.read(), encoding='utf-8')
        print(htmls)
        # return htmls
    def __analysis(self,htmls):
        a=1
        root_html=re.findall(Spilder.root_pattern,htmls)
        print(root_html)
    def go(self):
        self.__fetch_content()
        print('123')
        # self.__analysis(htmls)

spilder=Spilder()
spilder.go()