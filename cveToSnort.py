"""
ELI - 02/06/2020
CVE TO SNORT MIGRATION TOOL
---------------------------------------
1) Store the 10,000+ CVEs that your company is vulnerable to in a file called "cve". Make sure each CVE has its own line.
2) Run the script.
3) Go get coffee and hack things.
4) When complete, copy and paste the information stored in sidList.txt and send it to your SOC team.
5) All your SOC team has to do now is copy and paste the SIDs in their Snort environments, and you officilally have some form of mitigation in place!
------------------------------------------
"""
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
