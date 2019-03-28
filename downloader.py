from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(open("Tiger.html"), "html.parser")
for links in soup.find_all('a', href=re.compile("\.mp3")):
	print(links.get('href'))


