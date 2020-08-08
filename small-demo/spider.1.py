from urllib import request
# 断点调试!!!
# 这个爬虫不可以爬出斗鱼的分类页的数据,会存在字符的问题

# 解决ssl身份的问题
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class Spider():
    # url = "https://movie.douban.com/"
    url = "https://www.douyu.com/g_LOL"
    # 加头部,解决反爬418
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

    def __fetch_content(self):
        ret = request.Request(Spider.url, headers=Spider.headers)
        res = request.urlopen(ret)
        aa = res.read().decode('utf-8')
        print(aa)
        # byte
        # htmls = r.read()
        # htmls = str(htmls, encoding='utf-8')
        # a=1

    def __analysis(self, htmls):
        pass

    def go(self):
        self.__fetch_content()
        # self.__analysis(htmls)


spider = Spider()
spider.go()
