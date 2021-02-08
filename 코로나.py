import telegram

from bs4 import BeautifulSoup
import requests



req = requests.get("http://ncov.mohw.go.kr/")
#print(req.text)

soup = BeautifulSoup(req.text, "html.parser")
#print(soup)

국내, 해외 = soup.find("div", class_="liveNum_today_new").find_all("span", class_="data")

#print(국내.text, 해외.text)

합계 = int(국내.text) + int(해외.text)
#print(합계)

코로나 = "국내 발생 : " + 국내.text + "\n해외 발생 : " + 해외.text + "\n합계 : " + str(합계)
print(코로나)
