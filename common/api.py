#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :api.py
#@time   :2020/4/22 18:37
#@Author :jmgen
#@Version:1.0
#@Desc   :
"""
封装request

"""

import requests,json
from common.logger import Logger

log = Logger(name=__file__).get_logger()
TIMEOUT = 30
class Api:

    def __init__(self):
        """
        :param env:
        """
        self.session = requests.Session()
        self.STRESS_LIST=[]

    def to_request(self, method, url, **kwargs):
        if not url.startswith('https://'):
            url = '%s%s' % ('https://', url)
            log.info(url)
        kwargs['timeout'] = kwargs.get('timeout', TIMEOUT)
        log.info(f"请求数据: {method} {url} {kwargs}")
        try:
            res = self.session.request(method, url, **kwargs)
        except requests.RequestException as e:
            log.info('%s%s' % ('RequestException url: ', url))
            log.info(e)
            return ()
        except Exception as e:
            log.info('%s%s' % ('Exception url: ', url))
            log.info(e)
            return ()
        log.info(f"响应数据: {res.text}")

        time_consuming = res.elapsed.microseconds / 1000
        time_total = res.elapsed.total_seconds()
        self.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = res.status_code
        try:
            response_dicts['body'] = res.json()
        except Exception as e:
            log.info(e)
            response_dicts['body'] = ''
        response_dicts['text'] = res.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total
        return response_dicts

    def GET(self, url, **kwargs):
        return self.to_request('get', url, **kwargs)

    def POST(self, url, **kwargs):
        return self.to_request('post', url, **kwargs)

    def PUT(self, url, **kwargs):
        return self.to_request('put', url, **kwargs)

    def create_json(self):
        mesg = {"key": "value"}
        with open("test.json", "w") as f:
            json.dump(mesg, f)