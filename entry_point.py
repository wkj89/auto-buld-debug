# -*- coding:utf-8 -*-

# import requests
import os
import sys

code_url = os.environ.get('code_url', '')
if code_url == "":
    print('code_url env not set')
    sys.exit()
# code_url = "https://github.com/wkj89/auto-buld-debug/archive/master.zip"
cmd = 'wget %s' % code_url
tmp = os.popen(cmd).readlines()
exists = os.path.exists("/master.zip")
if not exists:
    print(u"download file err，url：%s" % code_url)
    print(tmp)

    sys.exit(1)
os.popen("mkdir code_tmp")
tmp = os.popen("unzip  master.zip -d code_tmp ").readlines()
dirs = os.listdir("/code_tmp")
if len(dirs) == 0:
    print(u'failed to unzip')
    print(tmp)

dir_name = dirs[0]

os.popen("mv /code_tmp/%s /code" % dir_name)

print(u"start run /code/entrypoint.sh ")
os.popen("./code/entrypoint.sh")

