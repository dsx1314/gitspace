# # import yagmail
# #
# # from ftzn.data.eamil_users import users
# #
# #
# # def send_test_report(subject, contents, report):
# #     mail = yagmail.SMTP(user='2986787982@qq.com',
# #                         password='ylzazpxljudvddhi',
# #                         host='smtp.qq.com')
# #
# #     mail.send(to=users(),
# #               subject=subject,
# #               contents=contents,
# #               attachments=report)
# #
# # if __name__ == '__main__':
# #     send_test_report('接口自动化测试报告','大师兄','F:\\pythonProject1\\ftzn\\reports\\index.html')
# #     print('----sucess----')
#
#
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.header import Header
#
# from ftzn.data.eamil_users import users
#
#
# def send_mail(report_name):
#
#     # receiver_users = users()
#     f = open(report_name,'rb')
#     mail_body = f.read()
#     f.close()
#
#     smtpsever = 'smtp.qq.com'
#
#     sender = '2986787982@qq.com'
#     password = 'ylzazpxljudvddhi'
#
#     receiver = users()
#
#     subject = '接口自动化测试报告'
#
#     print("----------------------------")
#     #  登录邮箱
#     server = smtplib.SMTP(smtpsever)
#     server.login(sender,password)
#
# #     添加附件
#     send_file = open(report_name,'rb').read()
#     att = MIMEText(send_file,'base64','utf-8')
#
#     att['Content-Type'] = 'application/octet-stream'
#
#     att['Content-Disposittion'] = 'attachment;file_name="index.html"'
#
#     msg = MIMEMultipart('related')
#     msgtext = MIMEText(mail_body,'html','utf-8')
#     msg.attach(msgtext)
#     msg["From"] = sender
#     msg["To"] = receiver
#     msg["Subject"] = Header(subject,'utf-8').encode()
#     msg.attach(att)
#
#     print("---------------------------")
# #     发送邮件
#     server.sendmail(sender,[receiver],msg.as_string())
#     server.quit()
#
#
# if __name__ == '__main__':
#     send_mail('F:\\pythonProject1\\ftzn\\reports\\index.html')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
