# _*_ coding:utf-8 _*_
__author__ = "Jianpan"
__date__ = "2017/11/4 下午7:44"

import urllib.request
import urllib.parse
import urllib.error

# file = urllib.request.urlopen('http://www.baidu.com')
# data = file.read()
# dataline = file.readline()
# print(data)
# print(dataline)

# 保存在本地  wb->二进制
# fhandle = open('/Users/jianpan/Documents/F/07python/01project/learn_crawler/baidu.html', 'wb')
# fhandle.write(data)
# fhandle.close()

# urllib.request.urlretrieve('http://edu.51cto.com',
#                            filename='/Users/jianpan/Documents/F/07python/01project/learn_crawler/51cto.html')
# urllib.request.urlcleanup()

# print(file.info())
# print(file.getcode())
# print(file.url)

# URL编码
# sina_quote = urllib.request.quote('http://www.sina.com.cn')
# print(sina_quote)

# URL解码
# sina_unquote = urllib.request.unquote(sina_quote)
# print(sina_unquote)

# 添加头部 Headers属性 浏览器的模拟
# url_csdn = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
# headers = ("User-Agent",
#            "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X)AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1")
# opener = urllib.request.build_opener()
# opener.addheaders = [headers]
# file_csdn = opener.open(url_csdn).read()
# fhandle_csdn = open('/Users/jianpan/Documents/F/07python/01project/learn_crawler/csdn.html', 'wb')
# fhandle_csdn.write(file_csdn)
# fhandle_csdn.close()
# print(file_csdn)

# 超时设置
# for i in range(1, 100):
#     try:
#         file = urllib.request.urlopen("http://yum,iqianyue.com", timeout=30)
#         data = file.read()
#         print(len(data))
#     except Exception as e:
#         print('出现异常 -->' + str(e))


# HTTP协议请求实战

# GET请求
'''
 1,构建对应的URL地址
 2,以URL构建Request对象
 3,通过urlopen()打开构建的Request对象
 4,按照需求进行后续的操作，比如网页内容读取，保存
'''
# keywd = 'hello'
# url = 'http://www.baidu.com/s?wd='+keywd
# req = urllib.request.Request(url)
# data = urllib.request.urlopen(req).read()
# fhandle_http_baidu = open('/Users/jianpan/Documents/F/07python/01project/learn_crawler/http_baidu.html','wb')
# fhandle_http_baidu.write(data)
# fhandle_http_baidu.close()

# keywd = '韦玮老师'
# url = 'http://www.baidu.com/s?wd='
# key_code = urllib.request.quote(keywd)
# req = urllib.request.Request(url + key_code)
# data = urllib.request.urlopen(req).read()
# fhandle_http_baidu = open('/Users/jianpan/Documents/F/07python/01project/learn_crawler/http_baidu_ww.html', 'wb')
# fhandle_http_baidu.write(data)
# fhandle_http_baidu.close()

# POST请求
'''
1，设置好URL地址
2，构建表单数据，并使用urllib.parse.urlencode对数据进行编码处理
3，创建Request对象，参数包括URL地址和要传递的参数
4，使用add_headers()添加头信息，模拟浏览器进行爬取
5，使用urllib.request,urlopen()打开对应的Request对象，完成信息传递
6，后续处理，比如网页读取，保存等
'''

# url = 'http://www.iqianyue.com/mypost'
# post_data = {
#     'name': 'jianpan',
#     'pass': '123456'
# }
# post_data_encode = urllib.parse.urlencode(post_data).encode('utf-8')
# req = urllib.request.Request(url, post_data_encode)
# req.add_header("User-Agent",
#            "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X)AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1")
# data = urllib.request.urlopen(req).read()
# fhandle = open('/Users/jianpan/Documents/F/07python/01project/learn_crawler/http_post.html', 'wb')
# fhandle.write(data)
# fhandle.close()

# 代理服务器设置
# 代理服务器地址，爬取的网页地址
# def use_proxy(proxy_addr, url):
#     proxy = urllib.request.ProxyHandler({'http': proxy_addr})
#     # 为了方便使用全局的opener对象
#     opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
#     urllib.request.install_opener(opener)
#     data = urllib.request.urlopen(url).read().decode('utf-8')
#     return data
#
#
# proxy_addr = '183.12.27.147	:8118'
# data = use_proxy(proxy_addr, 'http://www.baidu.com')
# print(len(data))


# 开启DebugLog
# httphd = urllib.request.HTTPHandler(debuglevel=1)
# httpshd = urllib.request.HTTPSHandler(debuglevel=1)
# opener = urllib.request.build_opener(httphd, httpshd)
# urllib.request.install_opener(opener)
# data = urllib.request.urlopen('http://edu.51cto.com')
# print(data)

#异常处理 URLError
try:
    print('-----------------------------start---------------------------------')
    file = urllib.request.urlopen('http://blog.csdn9898.net')
    print(file.readlines())
    print('-----------------------------end-----------------------------------')
except urllib.error.URLError as e:
    # print(e.code)
    print(e.reason)





