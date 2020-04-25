#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @file   :config.py
# @time   :2020/4/22 18:50
# @Author :jmgen
# @Version:1.0
# @Desc   :
import os
from configparser import ConfigParser
from common.logger import Logger

log = Logger(name=__file__).get_logger()


class Config:
    def __init__(self):
        """
        初始化
        """
        self.tests_path = 'testcase'
        self.report_path = 'report'

    class TestEnv:
        login_base_url = 'https://auth.feidee.cn'
        feidee_base_url = 'https://api.feidee.cn'
        device = '{"locale":"zh-Hans-CN","device_id":"6AD4E1E1-8553-4477-BFEA-B91E442A6E48","platform":"iPhone","model":"iPhone11,6","os_version":"13.3.1","product_version":"12.48.0","product_name":"MyMoney"}'
        login_headers = {
            # 'Host': 'auth.feidee.cn',
            'Nonce-Str': '4CDAC2E9EF4040EDA50F979C0122F740',
            'Device': device,
            'Client-Key': '213DB22363CE44C7B2F51E9549A8B5C6',
            'Sign': 'ab3372ddb612683e96eaedd277444075'
        }
        login_params = {"username": 'jmgen010@kd.ssj',
                        "scope": "accountbook;user",
                        "password": "7bca5282a041ca8bbd12ec2d98c83f30",
                        "grant_type": "password",
                        "encode_version": "v2"}

    class ProdEnv:
        login_base_url = 'https://auth.feidee.net'
        feidee_base_url = 'https://api.feidee.net'
        device = '{"locale":"zh-Hans-CN","device_id":"6AD4E1E1-8553-4477-BFEA-B91E442A6E48","platform":"iPhone","model":"iPhone11,6","os_version":"13.3.1","product_version":"12.48.0","product_name":"MyMoney"}'
        login_headers = {
            # 'Host': 'auth.feidee.net',
            'Nonce-Str': '02F7D2E3361745DEABA59AE2F486EBB6',
            'Device': device,
            'Client-Key': '5AA20FE4D8BC4B8A9A41B820045AFF8C',
            'Sign': '5e61e52f32b4d92a0379f35ac48def42'
        }
        login_params = {"username": 'jmgen029@me.com',
                        "scope": "accountbook;user",
                        "password": "7bca5282a041ca8bbd12ec2d98c83f30",
                        "grant_type": "password",
                        "encode_version": "v2"}


config = {
    "test": Config.TestEnv,
    "prod": Config.ProdEnv
}
