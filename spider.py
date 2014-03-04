import httplib
import urllib
import time
conn=httplib.HTTPConnection("www.ycxyz.com");

conn.request("GET","/ydzn/index.php/login/in.html");
r1=conn.getresponse();
print(r1.status,r1.reason)
cookie1 = r1.getheader("Set-Cookie")
cookie = cookie1[0:len("PHPSESSID=oudjq31uv3qm31rsl45det6t50")]
print cookie
data1=r1.read()
#print data1
params = urllib.urlencode({'pstudentid':'134611144','ppwd':'611144','statement':'1'})
conn.request("POST", "/ydzn/index.php/login/a_login.html",
 headers = {"Cookie": cookie,
 			"Host":"www.ycxyz.com"}, body = params);
r2 = conn.getresponse();
data2 = r2.read()
print data2
#POST /ydzn/index.php/login/a_login.html HTTP/1.1\r\n
#
conn.close()
