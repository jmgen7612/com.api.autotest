#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @file   :vaccinum_data.py
# @time   :2020/4/23 20:21
# @Author :jmgen
# @Version:1.0
# @Desc   :
class Vaccinum_data:
    class test_data:
        vaccinum_list_data = {
            "case_no": "",
            'caseinfo':'查询疫苗列表正常',
            'casedata': [('1','3634193'),('2','3634193')],
            'checkdata':{},
        }
        vaccinum_status_data = {
            "case_no": "",
            'caseinfo': '更新疫苗状态正常',
            'casedata':[('44','1','3634193'),('45','1','3634193')],
            'checkdata': {},
        }

    class prod_data:
        vaccinum_list_data = {
            "case_no": "",
            'caseinfo':'查询疫苗列表正常',
            'casedata': [('1', '3634193'), ('2', '3634193')],
            'checkdata': {},
        }
        vaccinum_status_data = {
            "case_no": "",
            'caseinfo': '更新疫苗状态正常',
            'casedata': [('32', '1', '55303987344'), ('31', '1', '55303987344')],
            'checkdata': {},
        }

casedata = {
        'test': Vaccinum_data.test_data,
        'prod': Vaccinum_data.prod_data,
        'default': Vaccinum_data.test_data
    }
