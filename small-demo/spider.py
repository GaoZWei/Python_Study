from urllib import request
from io import BytesIO
import re
import gzip
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 爬虫框架:Beautiful soup,scrapy
# 爬虫,反爬虫,反反爬虫
# ip封=>代理ip库
class Spider():

    url = 'https://www.douyu.com/g_LOL'
    # [\s\S]字符*0次或多次 ?非贪婪  ([\s\S]*?)
    root_pattern = '<div class="DyListCover-info">(.*?)</div>'  # 匹配所有内容,非贪婪
    # root_pattern = '<div class="DyListCover-content">(.*?)</div>'  没用上
    name_pattern = '<use xlink:href="#icon-user_c95acf8"></use></svg>([\s\S]*?)</h2>'
    number_pattern = '<use xlink:href="#icon-hot_8a57f0b"></use></svg>(.*?)</span>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()  # 返回byte
        buff = BytesIO(htmls)
        f = gzip.GzipFile(fileobj=buff)
        htmls = f.read().decode('utf-8')
        # htmls = str(htmls, encoding='utf-8')  不行
        # print(type(htmls))
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        # print(root_html)   findall返回list
        # print(type(root_html))   list
        # print(type(root_html[1]))  str
        root_html1 = []
        root_html1 = root_html[1::2]  # 取偶数项,切片操作 (数据特殊,必须是第二个孩子)
        # print(root_html1[1])
        anchors = []
        for html in root_html1:
            name = re.findall(Spider.name_pattern, html)  # list
            number = re.findall(Spider.number_pattern, html)  # list
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        return anchors

    def __refine(self, anchors):  # 数据精炼
        def l(anchor): return {  # 返回对象
            'name': anchor['name'][0].strip(),  # strip去空格
            'number': anchor['number'][0]
        }
        return map(l, anchors)  # 返回map

    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_sead, reverse=True)
        return anchors

    def __sort_sead(self, anchor):  # 配置sort的第二个参数
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])  # r[0]匹配的是开头数字
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            print('Rank '+str(rank+1)+':' +
                  anchors[rank]['name']+'  '+anchors[rank]['number'])

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()
