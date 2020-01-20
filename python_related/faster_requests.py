from __future__ import print_function, division, with_statement
import os
import sys
import time
import requests

start_t = time.time()
for _ in range(100):
    resp = requests.get('https://baidu.com').content.decode()
end_t = time.time()

print(f'访问一百次百度网页，耗时:{end_t-start_t}')

###################################################################################

