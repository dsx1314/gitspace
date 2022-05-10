

#-----------------发送邮件----------------------------
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

import sys,smtplib,time,os,unittest
from email.mime.text import MIMEText



def sendReport(file_new):

    #  多个接收邮箱单个收件人的话，直接是receiver = 'XXX@126.com'
    # receiver = 'xxx@163.com' #['XXX@126.com', 'XXX@126.com', 'XXX@doov.com.cn']
    sender = 'xxx@163.com'
    receiver = 'xxx@163.com'
    CC='xxx@163.com'

    # 附件的名称
    test_Time = str(time.strftime("%Y-%m-%d", time.localtime()))
    test_file_name = test_Time + "__Report.html"

    #创建一个带附件的实例
    msg = MIMEMultipart()  # 如果一封邮件中含有附件，那邮件的中必须定义multipart/mixed类型

    # 邮件对象
    msg['Subject']=Header(u'xx接口自动化测试报告')   #    邮件的主题，用到from email.header import Header
    msg['From']=sender#写邮件的人
    msg['To']=receiver   #主要发送给的人   多个收件人时：   ";".join(receiver)
    msg['Cc']=CC #抄送的人

    # 正文模块，获取最新的报告做为正文
    # with open(file_new, 'rb') as f:   此写法也可以
    #     msg_raw = f.read()

    msg_raw = open(file_new, "rb").read()
    msg_total= MIMEText(msg_raw, 'html','utf-8')  #构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype
                                                     # 传入'HTML'表示HTML格式, 最后一定要用utf-8编码保证多语言兼容性
    # 添加到MIMEMultipart:
    msg.attach(msg_total)

    # 附件模块
    mfile = MIMEApplication(open(file_new, "rb").read())

    # 添加附件的头信息

    mfile.add_header('Content-Disposition', 'attachment', filename=test_file_name)

    # 附件模块添加到MIMEMultipart:
    msg.attach(mfile)

    smtp=smtplib.SMTP_SSL('smtp.exmail.qq.com',port=465) #端口smtp
    smtp.login('xxx@163.com', "xxxxxx")#登录邮箱的账号密码
    smtp.sendmail(sender,receiver,msg.as_string()) #参数分别是发送者，接收者,第三个是把上面的发送邮件的内容变成字符串
    smtp.quit()  # 发送完毕后退出smtp
    print ('邮件发送成功，请查收!')
if __name__ == '__main__':
    test_report = '‎/Users/lidada/Tools/apache-tomcat-9.0.22/webapps/report'  # 测试报告所在目录
    filePath = '/Users/lidada/Tools/apache-tomcat-9.0.22/webapps/report/report' + now + '.html'  # 通过加入报告生成时间，区分报告名称，否则报告会被覆盖
    fp = open(filePath.encode(), 'wb')  # 打开文件，以二进制方式将结果写入文件
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'xx自动化测试报告', description=u'xx接口测试,接口详情见附件')
    runner.run(suite)  # 执行测试，调用测试套件返回结果

    fp.close()  # 关闭文件，打开文件后一定要关闭文件，否则会占用资源
    sendReport(filePath)  # 发送最新的测试报告
