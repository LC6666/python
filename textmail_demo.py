# -*-coding:utf-8 -*-
__author__ ="豆豆嗯嗯"

import smtplib
from email.mime.text import MIMEText
from email.header import Header

if __name__ =="__main__":
    print("发送文本邮件示例")
    #邮件发送者
    sender = "deep_test@126.com"

    #邮件接收地址列表
    receivers = "ebmlc@ebmsz.com"

    #发送内容构建
    #text标识发送内容为文本格式
    msg = MIMEText("微信公众号：豆豆嗯嗯","plain","utf-8")
    msg['From'] = "deep_test@126.com"
    msg['To'] = receivers

    # 构建邮件标题
    msg['Subject'] = Header("开源优测_DeepTest","utf-8")

    # smtp服务
    smtpserver = "smtp.126.com"
    smtpport = 25

    # 发送人邮件用户名或专用于smtp账户用户名
    username = "deep_test"

    # 发送人邮件密码或专用于smtp账户的密码
    password = "123456a"

    # 构建smtp对象
    smtp = smtplib.SMTP()

    # 连接到smtp服务
    con = smtp.connect(smtpserver, smtpport)
    print("连接结果： ", con)

    # 登录smtp服务
    log = smtp.login(username, password)
    print("登录结果：", log)

    # 发送邮件
    print(receivers)
    res = smtp.sendmail(sender, receivers, msg.as_string())
    print("邮件发送结果： ", res)

    # 退出
    smtp.quit()
    print("send email finish")

