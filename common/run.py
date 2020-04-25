#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :run.py
#@time   :2020/4/23 12:08
#@Author :jmgen
#@Version:1.0
#@Desc   :
from common.shell import Shell,ls_by_key,dir_by_key
from common.logger import Logger
from config import config
import os,jprops,pytest,platform

log = Logger(name=__file__).get_logger()

class Run():
    def __init__(self):
        self.conf=config
        self.result_path =os.path.join(self.conf.Config().report_path,'result')
        self.html_report_path = os.path.join(self.conf.Config().report_path,'html')
        self.properties_path=os.path.join(self.result_path,'environment.properties')

    def get_run_args(self):
        #配置用于输出到报告的日志格式
        log_format = '--log-format=%(levelname)s %(asctime)s  %(message)s \n'.format()
        log_date_format = '--log-date-format=%H:%M:%S'
        log_level='--log-level={}'.format('info')

        args = ['-s', '-q',log_format,log_date_format,log_level,'--alluredir', self.result_path, "--verbose"]

        return args

    def generate_report(self,env):
        #给报告中添加执行环境信息
        env_dict={}
        env_dict.update(self.conf.config[env].__dict__)

        env_properties = {}
        for key0,value0 in env_dict.items():
            if(isinstance(value0,dict)):
                for key,value in value0.items():
                    env_properties['{}.{}'.format(key0,key)]=str(value)
            else:
                env_properties['{}.{}'.format(env,key0)] = str(value0)
        try:
            with open( self.properties_path,'w',encoding='utf-8') as fp:
                jprops.store_properties(fp, env_properties)
        except:
            log.error('配置环境未输出到报告中')

        #执行生成报告命令
        cmd = 'allure generate %s -o %s --clean' % (self.result_path, self.html_report_path)
        try:
            Shell.invoke(cmd)
            log.info("测试报告成功生成")
        except:
            log.error("Html测试报告生成失败,确保已经安装了Allure-Commandline")

    def exec(self,sys_argv):
        self._exec_pytest(sys_argv)
        # if len(sys_argv) != 0:
        #     self._exec_pytest(sys_argv)
        # else:
        #     # dir_tests = os.path.basename(self.conf.tests_path.get('tests'))
        #     self._batch_exec_pytest(sys_argv)

    def _exec_pytest(self,sys_argv):
        #读取命令行参数，单次执行
        args = sys_argv + self.get_run_args()
        pytest.main(args)

    def _batch_exec_pytest(self,sys_argv):
        # 并发执行用例
        args = sys_argv[:1]+ self.get_run_args()
        tests_path=str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, self.conf.Config().tests_path)))
        if(platform.system()=='Windows'):
            suitname_list=dir_by_key(tests_path,'test_')
        else:
            suitname_list = ls_by_key(tests_path, 'test_')
        pytest.main(args)
        # task=[]
        # print(sys_argv[:1][0])
        # for i in [x for x in range(int(sys_argv[1]))]:
        #     task.append(gevent.spawn(sys_argv[:1][0], i))
        # print(task)
        # gevent.joinall(task)