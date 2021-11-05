import requests
import time


class ErrorVK(Exception):
    def __init__(self, code, error):
        self.code = code
        self.error = error


class Captcha(Exception):
    def __init__(self, img):
        self.img = img


class API:
    __slots__ = ['session', 'app_id', 'v', 'token', 'data', 'owner_id', 'kwargs', 'url_api']

    def __init__(self, token, app_id=6146827, v="5.130", proxies=None):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'API'})
        if proxies is not None:
            self.session.proxies.update(proxies)
        self.app_id, self.v = app_id, v
        self.token = token
        self.data = {'access_token': self.token, "v": self.v, }

        self.kwargs = ()
        self.url_api = "https://api.vk.me/method/{}"

        self.owner_id = self.method('users.get')[0]['id']

    def method(self, name, p=None):
        result = self.http(method=False, url=self.url_api.format(name), data=(self.data if p is None else p | self.data)).json()
        if 'error' in result:
            if result['error']['error_code'] == 14:
                raise Captcha(result['error']['captcha_img'])
            else:
                if result['error']['error_code'] == 6:
                    time.sleep(0.4)
                raise ErrorVK(result['error']['error_code'], result['error']['error_msg'])
        else:
            return result['response']

    def http(self, method=True, **kwargs):
        self.kwargs = kwargs
        try:
            if method:
                return self.session.get(**kwargs)
            else:
                return self.session.post(**kwargs)
        except requests.exceptions.RequestException as ex:
            print('Error request:', ex)
