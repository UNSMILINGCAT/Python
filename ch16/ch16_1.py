import smtplib

fromAddress = '867974171@qq.com'
toAddress = '3418670057@qq.com'
msg = "这是一条测试邮件"
server = smtplib.SMTP("mail.113.110.170.79.com", 25)
server.sendmail(fromAddress, toAddress, msg)
