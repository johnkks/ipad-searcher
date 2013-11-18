#coding=gbk

import urllib2
import re
import time
import smtplib
from email.mime.text import MIMEText

mailto = ["364889036@qq.com"]

mail_host = "smtp.163.com"
mail_user = "15626238007@163.com"
mail_pass = "ipadmini2hehehe"
mail_postfix = "163.com"

me = mail_user+"<"+mail_user+"@"+mail_postfix+">"

def send_mail(to_list,sub,context):
	me = mail_user
	msg = MIMEText(context)
	msg['Subject'] = sub
	msg['From'] = me
	msg['To'] = ";".join(to_list)
	

	try:
		s = smtplib.SMTP(mail_host)
		s.login(mail_user,mail_pass)
		s.sendmail(me, to_list, msg.as_string())
		s.quit()
		print '1'
		return True
	except Exception, e:
		print '2'
		print str(e)
		return False








url = 'http://store.apple.com/cn/buy-ipad/ipad-mini-retina'

headers = {
                "GET":url,
                "Host":"store.apple.com",
                "Referer":"http://store.apple.com/cn/buy-ipad/",
                "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:24.0) Gecko/20100101 Firefox/24.0",
          }

req = urllib2.Request(url)
for key in headers:
	req.add_header(key,headers[key])
word = "暂无供应"



while True:
	page = urllib2.urlopen(req).read()
	ss = re.search(word,page)

	if ss == None :
		send_mail(mailto,"ipadmini2","mini2 is here \n http://store.apple.com/cn/buy-ipad/ipad-mini-retina")
		print "Yes"
		break
	else:
		print "No"
		time.sleep(1800)
