import requests
from parsel import Selector

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2837.0 Safari/537.36',
    'Cookie': ''
}
s = requests.Session()

r = s.get('http://58.42.251.237:8081/wechat/login.aspx', headers=headers)
set_cookie = r.headers['set-cookie']
headers['Cookie'] += set_cookie
hxs = Selector(text=r.text)
data = {
    '__EVENTTARGET': 'btnLogin',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': hxs.xpath('//input[@name="__VIEWSTATE"]/@value').extract_first(),
    '__EVENTVALIDATION': hxs.xpath('//input[@name="__EVENTVALIDATION"]/@value').extract_first(),
    'txtUserName': 'xxx',
    'txtPassword': 'xxx',
    'F_CHANGED': 'false',
    'F_TARGET': 'btnLogin',
    'F_STATE': 'e30=',
    'F_AJAX': 'true',
}
headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
headers['Content-Length'] = 382
r = s.post('http://58.42.251.237:8081/wechat/login.aspx', data=data, headers=headers)
set_cookie = r.headers['set-cookie']
set_cookie = str(set_cookie).replace('HttpOnly', '').split(';')[0]
headers['Cookie'] += set_cookie
del headers['Content-Length']
headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
headers['Accept-Encoding'] = 'gzip, deflate, sdch'
headers['Accept-Language'] = 'zh-CN,zh;q=0.8,en;q=0.6'
headers['Connection'] = 'keep-alive'
headers['Host'] = '58.42.251.237:8081'
headers['Referer'] = 'http://58.42.251.237:8081/wechat/Default.aspx'
headers['Upgrade-Insecure-Requests'] = '1'
headers['Cookie'] = headers['Cookie'].replace('HttpOnly', '')
r = s.get('http://58.42.251.237:8081/wechat/BD/AcceptancePlatform/AcceptanceQuery.aspx?SysNodeID=SMM-AcceptanceQuery', headers=headers).text
hxs = Selector(text=r)
data = hxs.xpath('//*[contains(text(), "var f2_state ")]/text()').extract_first()

