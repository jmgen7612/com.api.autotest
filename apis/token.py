#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :token.py
#@time   :2020/4/22 18:47
#@Author :jmgen
#@Version:1.0
#@Desc   :
"""
封装获取token方法

"""
from common.api import Api
from common.logger import Logger
from config import config

log = Logger(name=__file__).get_logger()
class Token:
    def __init__(self):
        self.config = config
        self.api=Api()

    def get_token(self, env):
        """
        获取token
        :param env: 环境变量
        :return:
        """
        url='/v2/oauth2/authorize'
        login_url = '{}{}'.format(self.config.config[env].login_base_url , url)
        headers= self.config.config[env].login_headers
        params = self.config.config[env].login_params

        response = self.api.GET(login_url, headers=headers,params=params)

        access_token=response.get('body').get('access_token')
        token_type = response.get('body').get('token_type')
        log.info(response.get('body'))
        log.debug('token: %s' % access_token)
        token=f"{token_type} {access_token}"
        return token