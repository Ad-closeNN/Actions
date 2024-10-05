from bs4 import BeautifulSoup
import requests
url = "https://profile-counter.glitch.me/WForst_Breeze/count.svg"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'xml')
numbers = ''.join([tspan.get_text() for tspan in soup.find_all('tspan')])

from datetime import datetime, timedelta, timezone
time_zone = timezone(timedelta(hours=8))
time = datetime.now(time_zone)
time_strftime = time.strftime("%Y/%m/%d %H:%M:%S")
print("当前时间：",time_strftime,"\n# 访问量：", numbers)