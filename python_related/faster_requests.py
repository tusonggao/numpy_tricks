from __future__ import print_function, division, with_statement
import os
import sys
import time
import requests

start_t = time.time()
for _ in range(100):
    resp = requests.get('https://baidu.com').content.decode()
end_t = time.time()

print(f'不使用Session 访问一百次百度网页，耗时:{end_t-start_t}')

###################################################################################

start_t = time.time()
session = requests.Session()
for _ in range(100):
    resp = session.get('https://baidu.com').content.decode()
end_t = time.time()

print(f'使用Session 访问一百次百度网页，耗时:{end_t-start_t}')

# 运行结果，输出如下：
# 不使用Session 访问一百次百度网页，耗时:22.324612855911255
# 使用Session 访问一百次百度网页，耗时:5.712132453918457
