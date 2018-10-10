from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import sys
from pathlib import Path
import os.path

now = datetime.datetime.now()

def main(symbols):
	for i in range(len(symbols)):
		try:
			html = urlopen("https://finance.yahoo.com/quote/"+symbols[i]+"/")
		except HTTPError as e:
			print(e)
		except URLError:
			print("Server down or incorrect domain")
		else:
			if not(os.path.isfile(symbols[i]+now.strftime("%Y-%m-%d")+".txt")):
				f = open(symbols[i]+now.strftime("%Y-%m-%d")+".txt", "x")
				res = BeautifulSoup(html.read(), "html5lib");
				label_tags = res.findAll("td", {"class": "C(black) W(51%)"})
				data_tags = res.findAll("td", {"class": "Ta(end) Fw(b) Lh(14px)"})
				f.write(symbols[i]+"\n")
				f.write(now.strftime("%Y-%m-%d")+"\n")
				for i in range(len(label_tags)):
					f.write(label_tags[i].getText()+": "+data_tags[i].getText()+"\n")

if __name__ == "__main__":
	main(sys.argv[1:])