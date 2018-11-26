#!/usr/bin/env python
# Coded By: Dwirn
# Twitter: @dwirn1337
# Telegram: @dwirn1337
# Github: github.com/dwirn1337
# WhatsApp: +55 11 94380-9900


from sys import argv
from os import system
from socket import gethostbyname

try:
   import requests
except:
   system("pip install --upgrade pip")
   system("pip install requests")
   import requests

def main(url):
   URL = 'http://www.crimeflare.org/cgi-bin/cfsearch.cgi'
   requests.get(URL)
   payload = {'cfS':url}
   SERVER_RESP = (requests.post(URL, data=payload).text)

   if url.startswith("http://") == True:
      url = url[7:]
   if url.startswith("https://") == True:
      url = url[8:]
   ip = gethostbyname(url)

   if "these are not CloudFlare-user nameservers" in SERVER_RESP:
      print ("\033[1;32m[!] IP encontrado: \033[1;37m{}\033[0m".format(ip))
   else:
      arq = open('res_cf.txt','w')
      arq.write(SERVER_RESP)
      arq.close()
      arq = open('res_cf.txt','r')
      linhas = arq.readlines()

      for res in linhas:
         if res.startswith('<LI>'):
            SS = res.split(" ")
            print ("\033[1;32m[!] Real IP encontrado: \033[1;37m{}\033[0m".format(SS[2]))
            print ("\033[1;32m[!] CloudFlare IP: \033[1;37m{}\033[0m".format(ip))
            break

if __name__ == '__main__':
   try:
      url1 = argv[1]
   except:
      print ("[+] Use: {} <url>".format(argv[0]))
      exit(0)

   if url1.startswith("http://") == False and url1.startswith("https://") == False:
      url1 = "https://{}".format(url1)

   main(url1)
