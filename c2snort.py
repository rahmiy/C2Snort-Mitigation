import requests
from bs4 import BeautifulSoup

#Remember to have a file named "cve" which stores all your CVEs, line by line.
CVE_Collection = [line.rstrip('\n') for line in open('cve')]
length = len(CVE_Collection)
f = open('sidList.txt','w')
f.close()
for i in range (0, length):
	cve = CVE_Collection[i]
	url = "https://www.snort.org/rule_docs?utf8=%E2%9C%93&rules_query=" + cve + "&search_type=standard&submit_rule_search="
	x = requests.get(url)	
    
   	if 'Search returned' in x.text:
		soup = BeautifulSoup(x.text,'lxml')
		for tag in soup.find_all('span',{"class":"categories"}):
			with open('sidList.txt','a') as afile:
				afile.write(tag.text +'\n')
				print ("SID: " + tag.text + " found.") 
