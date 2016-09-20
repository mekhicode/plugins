# encoding: utf-8
#!/usr/bin/env python

from splinter import Browser
import xlrd
import re
import requests


def from_local():
    discountcode = ""
    # username = data[9]
    url = "http://www.lookfantastic.com/decleor-anti-ageing-iconic-collection/10977987.html"
    username = u"mekhi"
    province = u"北京"
    city = u"北京"
    area = u"朝阳区"
    address = u"xxx"
    postCode = int("100000")
    phone = "12345678901"


    r = requests.get(url)
    get_url = r.url
    if "com" in get_url.split('/')[2]:
        create_account_url = "https://www.lookfantastic.com/lfint/accountCreate.account"
        login_url = "https://www.lookfantastic.com/lfint/login.jsp"
        basket_url = "https://www.lookfantastic.com/lfint/my.basket"
        country = "com"
    else:
        create_account_url = "https://www.lookfantastic.cn/lfcn/accountCreate.account"
        login_url = "https://www.lookfantastic.cn/lfcn/login.jsp"
        basket_url = "https://www.lookfantastic.cn/lfcn/my.basket"
        country = "cn"


    browser = Browser()

    # 注册
    # browser.visit(create_account_url)
    # browser.find_by_id('customerName').fill(username)
    # browser.find_by_id('customerEmail').fill(email)
    # browser.find_by_id('confirmCustomerEmail').fill(email)
    # browser.find_by_id('customerPassword').fill(password)
    # browser.find_by_id('confirmPassword').fill(password)

    # 登陆
    browser.visit(login_url)
    browser.find_by_id('username').fill("xxx")
    browser.find_by_id('password').fill("xxx")
    browser.find_by_id('login-submit').click()

    # 购买
    # for url in urls:
    #     browser.visit(url)
    #     if qty[0] == '1':
    #         pass
    #     else:
    #         browser.find_by_name('quantity').fill('2')
    browser.visit(url)
    browser.find_by_xpath('//p[@class="product-simple"]/span/a[@rel="nofollow"]').click()

    # 购物车
    browser.visit(basket_url)
    # 输入优惠码
    if discountcode:
        browser.find_by_name('discountCode').fill(discountcode)
        browser.find_by_id('add-discount-code').click()

    # 结算页面
    browser.find_by_id('gotocheckout2').click()

    import time
    time.sleep(10)


    browser.find_by_id('add-new-address').click()


    browser.find_by_id('delivery-addressee').fill(username)
    browser.find_by_id('delivery-state-province').fill(province)
    browser.find_by_id('delivery-town-city').fill(city)
    browser.find_by_id('delivery-street-name').fill(area)
    browser.find_by_id('delivery-name-number').fill(address)
    browser.find_by_id('delivery-post-zip-code').fill(postCode)
    browser.find_by_id('order-contact-number').fill(phone)


    import time
    time.sleep(3)

    browser.find_by_id('pay-with-alipay').click()

    import time
    time.sleep(3)

    browser.find_by_id('submit-my-order').click()


import time
start = time.time()
from_local()
end = time.time()
print end-start


def test():
    browser = Browser()
    print dir(browser)

# test()
