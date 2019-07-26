# -*- coding:utf-8 -*-

# import requests
import os
import sys

code_url = os.environ.get('code_url','')
if code_url =="":
    print('code_url env not set')
    sys.exit()
# code_url = "https://github.com/wkj89/hello-grpc/archive/master.zip"
cmd = 'wget %s' % code_url
tmp = os.popen(cmd).readlines()
exists = os.path.exists("/master.zip")
if not exists:
    print("下载文件失败，url：%s", code_url)
    print(tmp)

    sys.exit(1)
os.popen("mkdir code ")
tmp = os.popen("unzip  master.zip -d code ").readlines()
dirs = os.listdir("/code")
if len(dirs) == 0:
    print('解压缩失败')
    print(tmp)

dir_name = dirs[0]

os.popen('./code/%s/entrypoint.sh', dir_name)

