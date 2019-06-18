#coding=utf-8
import urllib.request
import re
import threading
import requests
import time
import os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
default_path = './ts/'

def download(url, name):
  try:
    urllib.request.urlretrieve(url, name)
    print(name)
  except:
    print("error : " + url)
imgurl = input("输入链接地址：")
min_util = input("输入下限：")
max_util = input("输入上限：")
sleep_s = float(input("输入下载间隔（s）："))
if_cover_exist_file = input("当发现文件存在是否覆盖(y/n)：")
try:
  min_util = int(min_util)
  max_util = int(max_util)
  for i in range(min_util, max_util + 1):
    # {:0>2d}     # 左侧补0
    # >>> "{:0>4d}".format(1)
    # '0001'
    imgurl = imgurl.format(i)
    # "https://doubanzyv4.tyswmp.com:888/2019/02/07/06SfTJsUSa6nKqG9/out" + contact_id + ".ts"
    # print(imgurl)
    try: 
      # urllib.request.urlretrieve(imgurl, '%s.ts' % (contact_id))
      if not os.path.exists(default_path):
        os.makedirs(default_path)
      download_path = default_path + '%s.ts' % (i)
      if os.path.exists(download_path) and (if_cover_exist_file == 'y'):
        os.remove(download_path)
      if not os.path.exists(download_path):
        try:
          urllib.request.urlopen(imgurl)
          p = threading.Thread(target=download,args=(imgurl, download_path))
          p.start()
          time.sleep(sleep_s)
        except:
          "ok"
    except:  
      print("error")
      # break
except:
  "error"
      
      