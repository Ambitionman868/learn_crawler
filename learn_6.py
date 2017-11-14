# _*_ coding:utf-8 _*_
__author__ = "Jianpan"
__date__ = "2017/11/7 上午7:15"

import re
import urllib.request
import ssl
import time
import urllib.error
# 全局取消证书验证

ssl._create_default_https_context = ssl._create_unverified_context


# 爬取京东手机图片
def craw(url, page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pattern1 = '<div id="plist".+? <div class="page clearfix">'
    result1 = re.compile(pattern1).findall(html1)
    result1 = result1[0]
    pattern2 = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    imagelist = re.compile(pattern2).findall(result1)
    x = 1
    print('---------------------start--------------------')

    for imgurl in imagelist:
        imgname = '/Users/jianpan/Documents/F/07python/img/' + str(page) + '_' + str(x) + '.jpg'
        imgurl = 'http://' + imgurl

        try:
            urllib.request.urlretrieve(imgurl, filename=imgname)

        except urllib.error.URLError as e:

            if hasattr(e, 'code'):
                x += 1
            if hasattr(e, 'reason'):
                x += 1
        x += 1

    print('---------------------end--------------------')


# for i in range(0,79):
#     url = 'http://list.jd.com/list.html?cat=9987,653,655&page='+str(i)
#     craw(url,i)

# 链接爬虫实战
def getlink(url):
    headers = ("User-Agent",
               "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X)AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 将opener安装为全局
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    # 根据需求构建好链接表达式
    pattern = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pattern).findall(data)
    # 去除重复元素
    link = list(set(link))
    return link


# url = 'http://blog.csdn.net/'
# linklist = getlink(url)
# for link in linklist:
#     print(link[0])

# 糗事百科
# def getcontent(url, page):
#     headers = ('User-Agent',
#                'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1')
#     opener = urllib.request.build_opener()
#     opener.addheaders = [headers]
#     # 将opener安装为全局
#     urllib.request.install_opener(opener)
#     data = urllib.request.urlopen(url).read().decode('utf-8')
#     #print(data)
#     # 构建对应用户提取的正则表达式
#     userpat = '<h2>(.*?)</h2>.*?</a>.*?<div.*?class'
#     # 构建段子内容提取的正则表达式
#     contentpat = '<div class="content">(.*?)</div>'
#
#     userlist = re.compile(userpat, re.S).findall(data)
#     contentlist = re.compile(contentpat, re.S).findall(data)
#     x = 1
#     for content in contentlist:
#         content = content.replace("\n", '')
#         print(content)
#         name = "content" + str(x)
#         #exec(name + '=content')
#         x += 1
#
#     y = 1
#
#     for user in userlist:
#         name = 'content' + str(y)
#         print("用户" + str(page) + str(y) + "是：" + user)
#         print('内容是：')
#         #exec('print(' + name + ')')
#         print('\n------------------------------------------------------------------')
#         y += 1
#
#
# for i in range(1, 2):
#     url = 'http://www.qiushibaike.com/8hr/page/' + str(i)
#     getcontent(url, i)


# 微信爬虫
headers = ('User-Agent',
           'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1')

opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
# 存储文字网址列表
listurl = []


# 使用代理服务器
def use_proxy(proxy_addr, url):
    try:
        proxy = urllib.request.ProxyHandler({'http': proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        print(data)
        print('----------------------------------------------------------------------')
        return data

    except urllib.error.URLError as e:

        if hasattr(e, 'code'):
            print(e.code)

        if hasattr(e, 'reason'):
            print(e.reason)

        time.sleep(10)
    except Exception as e:

        print('exception:' + str(e))
        time.sleep(1)


# 获取所有文章链接

def getlisturl(key, pagestart, pageend, proxy):
    try:
        page = pagestart
        keycode = urllib.request.quote(key)
        pagecode = urllib.request.quote('&page=')

        for page in range(pagestart, pageend + 1):
            url = 'http://weixin.sogou.com/weixin?type=2&query=' + keycode + pagecode + str(page)
            data1 = use_proxy(proxy, url)
            listurlpat = '<div class="txt-box">.*?(http://.*?)"'
            listurl.append(re.compile(listurlpat).findall(data1))

        print("共获取到" + str(len(listurl)) + "页")
        return listurl


    except urllib.error.URLError as e:

        if hasattr(e, 'code'):
            print(e.code)

        if hasattr(e, 'reason'):
            print(e.reason)

        time.sleep(10)
    except Exception as e:

        print('exception:' + str(e))
        time.sleep(1)


proxy = '119.29.158.87:80'
getlisturl('物联网', 1, 30, proxy)
