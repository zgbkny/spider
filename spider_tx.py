import httplib
import urllib
import time
import gzip
conn=httplib.HTTPConnection("www.ycxyz.com");
conn.request("GET","/ydzn/index.php/login/in.html");
r1=conn.getresponse();
print(r1.status,r1.reason)
cookie1 = r1.getheader("Set-Cookie")
cookie = cookie1[0:len("PHPSESSID=oudjq31uv3qm31rsl45det6t50")]
print cookie
data1=r1.read()
conn.close()

conn=httplib.HTTPConnection("www.ycxyz.com");
for i in range(1,200000,1):
	conn.request("GET", "/ydzn/index.php/ucenter/show/"+str(i)+".html", 
		headers = {"Cookie":"PHPSESSID=8flariqirl3hvchmd02d3jbsl6",
				   "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:27.0) Gecko/20100101 Firefox/27.0",
				   "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
				   "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
				   "Accept-Encoding":"gzip, deflate",
				   "Connection":"keep-alive"})
	r1=conn.getresponse();
	print(r1.status,r1.reason)
	
	data1=r1.read()
	output = open('/home/ww/cache/data_gzip/'+str(i)+'.html', 'wb')
	output.write(data1)
	output.close()
	content = gzip.GzipFile('/home/ww/cache/data_gzip/'+str(i)+'.html', 'rb').read();
	print content
	output = open('/home/ww/cache/data_html/'+str(i)+'ok.html', 'w')
	output.write(content)
	output.close()
#POST /ydzn/index.php/login/a_login.html HTTP/1.1\r\n
#
conn.close()