# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
from .config import Config
from .logger import log


class Email:
    """Email类，读取配置中的基本配置，初始化要求title必填，message与文件路径可选"""
    def __init__(self, title, message=None, path=None):
        """调用Config类，读取配置"""
        cf = Config()
        self.server = cf.get('email', 'server')
        self.sender = cf.get('email', 'from')
        self.receiver = cf.get('email', 'to')
        self.password = cf.get('email', 'pass')
        self.title = title
        self.message = message
        self.file = path

    def send(self):
        """发送邮件"""
        msg = MIMEMultipart('related')
        msg['Subject'] = self.title
        msg['From'] = self.sender
        msg['To'] = self.receiver
        if self.message:
            msg.attach(MIMEText(self.message))
        # 附上文件
        if self.file:
            att = MIMEText(open('%s' % self.file, 'rb').read(), 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            filename = re.split(r'[\\|/]', self.file)
            att["Content-Disposition"] = 'attachment; filename="%s"' % filename[-1]
            msg.attach(att)
        # 连接服务器并发送
        try:
            smtp_server = smtplib.SMTP(self.server)
            smtp_server.login(self.sender, self.password)
            smtp_server.sendmail(self.sender, self.receiver.split(';'), msg.as_string())
            log('mail', u'发送邮件\'%s\'成功!' % self.title, 'info')
        except Exception, e:
            log('mail', e, 'error')
        finally:
            smtp_server.quit()


if __name__ == '__main__':
    tit = u'测试报告'
    tex = '这是今天的测试报告！请查看'
    # f = 'D:\\py\\1.py'
    email = Email(title=tit, message=tex)
    email.send()