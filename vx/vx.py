# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import hashlib
from wechat_sdk import WechatConf
conf = WechatConf(
    token='test',  # 你的公众号Token
    # appid='',  # 你的公众号的AppID
    # appsecret='',  # 你的公众号的AppSecret
    encrypt_mode='normal',  # 可选项：normal/compatible/safe，分别对应于 明文/兼容/安全 模式
    # encoding_aes_key='your_encoding_aes_key'  # 如果传入此值则必须保证同时传入 token, appid
)

from wechat_sdk import WechatBasic
wechat = WechatBasic(conf=conf)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        signature = self.get_argument('signature', 'default')
        timestamp = self.get_argument('timestamp', 'default')
        nonce = self.get_argument('nonce', 'default')
        echostr = self.get_argument('echostr', 'default')
        if signature != 'default' and timestamp != 'default' and nonce != 'default' and echostr != 'default' \
                and wechat.check_signature(signature, timestamp, nonce):
            self.write(echostr)
        else:
            self.write('Not Open')

class TestHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        pass

def make_app():
    return tornado.web.Application([
        (r"/vx", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()