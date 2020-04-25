#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :shell.py
#@time   :2020/4/22 18:42
#@Author :jmgen
#@Version:1.0
#@Desc   :
import subprocess,platform
from common.logger import Logger
log = Logger(name=__file__).get_logger()
class Shell:
    @staticmethod
    def invoke(cmd,cwd=None,is_log=True):
        # shell设为true，程序将通过shell来执行
        # stdin, stdout, stderr分别表示程序的标准输入、输出、错误句柄。
        # 他们可以是PIPE，文件描述符或文件对象，也可以设置为None，表示从父进程继承。
        # subprocess.PIPE实际上为文本流提供一个缓存区
        if is_log==True:
            log.info("执行命令: {}".format(cmd))
        p= subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,cwd=cwd)
        output, errors=p.communicate()
        if (platform.system() == 'Windows'):
            out = output.decode("utf-8", "ignore")
        else:
            out = output.decode("utf-8")
        return out

def ls_by_key(path: str, key: str):
    # 获取当前路径下,通过ls命令获取的文件或文件夹名的列表,过滤条件为对应的key参数
    # 输出list
    result = []
    out = Shell.invoke('ls', cwd=path, is_log=False)
    for ele in out.splitlines():
        if key in ele:
            result.append(ele)
    return result

def dir_by_key(path: str, key: str):
    # 获取当前路径下,通过dir命令获取的文件或文件夹名的列表,过滤条件为对应的key参数
    # 输出list
    result = []
    out = Shell.invoke('dir', cwd=path, is_log=False)
    for ele in out.splitlines():
        if key in ele:
            result.append(ele.split(' ')[-1])
    return result