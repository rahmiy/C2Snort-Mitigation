import requests

#Remember to have a file named "cve" which stores all your CVEs, line by line.
CVE_Collection = [line.rstrip('\n') for line in open('cve')]
length = len(CVE_Collection)
f = open('sidList.txt','w')
f.close()

# for statement that goes through all CVEs line by line
for i in range (0, length):
    cve = CVE_Collection[i]
    url = "https://www.snort.org/rule_docs?utf8=%E2%9C%93&rules_query=" + cve + "&search_type=standard&submit_rule_search="
        r = requests.get(url)
        
       if 'Search returned' in r.text:
            a = r.text
                pre = a.rfind('<span class="categories">')
            index2 = a.find('<',pre + len('<span class="categories">'))
            SID = (a[pre + len('<span class="categories">'):index2])
            print (cve + " - SID has been found. Storing: " + SID )
            with open('sidList.txt', 'a') as afile:
            afile.write(SID+'\n')
