#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :test_vaccinum.py
#@time   :2020/4/22 20:31
#@Author :jmgen
#@Version:1.0
#@Desc   :
import pytest,allure
import pytest_check as check
from apis.vaccinum_api.vaccinum_api import Vaccinum
from testdata.vaccinum_data import casedata
# from urllib.parse import urljoin

@allure.feature("疫苗接口")
@allure.description('疫苗接口查询和更新')
class Test_vaccinum(Vaccinum):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story(casedata['default'].vaccinum_list_data.get('caseinfo'))
    @pytest.mark.parametrize('type,tradingEntity', casedata['default'].vaccinum_list_data.get('casedata'))
    # @pytest.mark.parametrize('type,tradingEntity', [('1', '55303987344')])
    # @pytest.mark.parametrize('type,tradingEntity', [('1', '3634193')])
    def test_vaccinum_list_001(self, type, tradingEntity):
        """查询疫苗列表"""
        res=self.vaccinum_list( type, tradingEntity)
        # 响应断言
        check.equal(200, res.get('code'))

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story(casedata['default'].vaccinum_status_data.get('caseinfo'))
    @pytest.mark.parametrize('vaccinumId,status,tradingEntity', casedata['default'].vaccinum_status_data.get('casedata'))
    # @pytest.mark.parametrize('vaccinumId,status,tradingEntity', [('32', '1', '55303987344')])
    # @pytest.mark.parametrize('vaccinumId,status,tradingEntity', [('44', '1', '3634193')])
    def test_vaccinum_status_002(self, vaccinumId, status, tradingEntity):
        """更新疫苗状态"""
        res = self.vaccinum_status(vaccinumId, status, tradingEntity)
        #  响应断言
        check.equal(200, res.get('code'))