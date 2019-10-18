#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import time
import hashlib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


# 配置蒲公英KEY
API_KEY = "xxxxxxxxxxxxxxxxxxxx"
# 配置蒲公英更新描述信息
PGYER_DESC = "xxxxxxxxxxxxxxxxxxxx"

# 邮件信息
from_addr = "xxxx@163.com"
password = "xxxxxxxx"
smtp_server = "smtp.163.com"
to_addr = 'xxxx@xx.com'


# 打包apk
def build_apk():
    print "exporting..."
    
    build_com = "./gradlew assembleRelease"
    os.system(build_com)

#上传蒲公英
def upload_Pgyer():
    print "uploading..."

    apk_path = "./app/build/outputs/apk/release/app-release.apk"
    print "apk_path:"+apk_path
    apk_path = os.path.expanduser(apk_path)
    upload_com = "curl -F 'file=@%s' -F '_api_key=%s' -F 'buildUpdateDescription=%s' https://www.pgyer.com/apiv2/app/upload" % (apk_path,API_KEY,PGYER_DESC)
    os.system(upload_com)
    print "\n** UPLOAD TO PGYER SUCCEED **\n"

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
    
# 发邮件
def send_mail():
    print "sending..."
    
    msg = MIMEText('Android测试项目已经打包完毕，请前往 https://www.pgyer.com/xxxxx 下载测试！', 'plain', 'utf-8')
    msg['From'] = _format_addr('自动打包系统 <%s>' % from_addr)
    msg['To'] = _format_addr('测试人员 <%s>' % to_addr)
    msg['Subject'] = Header('Android客户端打包程序', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    print "\n** SEND EMAIL SUCCEED **\n"

def main():
    # 打包apk
    build_apk()
    # 上传蒲公英
    upload_Pgyer()
    # 发邮件
    send_mail()

# 执行
main()
