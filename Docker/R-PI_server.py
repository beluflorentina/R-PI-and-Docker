import os
import re
import requests

os.system("arp -a>> arp.txt")
with open("arp.txt", "r+") as arp:#r+ for updating the file=trincate
    arp_list=list(arp.readlines())
    #print(lista_arp)
    for i in arp_list:
        #if "00:50:56:f0:b0:45" in i:
        if "at e4:5f:01:db:99:40" in i:#r-pi mac address
            pattern="\((.*)\)"# .= any character, *=zero or more occurances
            result=re.findall(pattern, str(i))

            #deleteing the lines wrote
            arp.seek(0)
            arp.truncate()
            #print(result[0])
            break

api_url="http://"+result[0]+":5000/"
response=requests.get(api_url)
print(response.content)
