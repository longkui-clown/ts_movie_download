#coding=utf-8
import urllib.request
import re
import threading
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

min_util = input("输入下限：")
max_util = input("输入上限：")
if_cover_exist_file = input("当发现文件存在是否覆盖(y/n)：")
try:
  min_util = int(min_util)
  max_util = int(max_util)
  contact_id = "001"
  for i in range(min_util, max_util + 1):
    if i < 10:
      contact_id = "00" + str(i)
    elif i < 100:
      contact_id = "0" + str(i)
    else:
      contact_id = str(i)
    imgurl = "https://doubanzyv4.tyswmp.com:888/2019/02/07/06SfTJsUSa6nKqG9/out" + contact_id + ".ts"
    # print(imgurl)
    try: 
      # urllib.request.urlretrieve(imgurl, '%s.ts' % (contact_id))
      if not os.path.exists(default_path):
        os.makedirs(default_path)
      download_path = default_path + '%s.ts' % (contact_id)
      if os.path.exists(download_path) and (if_cover_exist_file == 'y'):
        os.remove(download_path)
      if not os.path.exists(download_path):
        try:
          urllib.request.urlopen(imgurl)
          p = threading.Thread(target=download,args=(imgurl, download_path))
          p.start()
          time.sleep(0.5)
        except:
          "ok"
    except:  
      print("error")
      # break
except:
  "error"
      
      