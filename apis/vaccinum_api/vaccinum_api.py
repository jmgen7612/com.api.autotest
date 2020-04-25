#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @file   :vaccinum_api.py
# @time   :2020/4/23 20:28
# @Author :jmgen
# @Version:1.0
# @Desc   :
from config import config
from apis.token import Token
from config.env import ENV
from common.api import Api

class Vaccinum:
    api = Api()
    token = Token()
    base_url = config.config[ENV].feidee_base_url
    headers = {"Authorization": token.get_token(ENV),
               "Device": config.config[ENV].device,
               }

    def vaccinum_list(self, type, tradingEntity):
        """查询疫苗列表"""
        url = ('/v1/vaccinum/{}/{}/list'.format(type, tradingEntity))
        res = self.api.GET('{}{}'.format(self.base_url, url), headers=self.headers)
        return res

    def vaccinum_status(self, vaccinumId, status, tradingEntity):
        """更新疫苗状态"""
        url = '/v1/vaccinum/modifyStatus'
        self.headers['Content-Type'] = 'application/json; charset=UTF-8'

        json_data = {"vaccinumId": vaccinumId,
                     "status": status,
                     "tradingEntity": tradingEntity,
                     }
        res = self.api.POST('{}{}'.format(self.base_url, url), headers=self.headers, json=json_data)
        return res