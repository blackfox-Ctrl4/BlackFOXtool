import bs4
import requests
import socket
from warnings import filterwarnings
from ipwhois import IPWhois
import time
import hashlib
import os
import sys
import webbrowser
from helplist import helpp
from modules import sha256

try:
  from colorama import Fore
except:
  os.system(Fore.RED+"clear ; echo '[!] installing colorama [!]' ; pip3 install colorama ; echo '[?] Done [?]'")

#---------------------------------------------

try:
  import requests
except:
  os.system(Fore.RED+"clear ; echo '[!] installing requests [!]' ; pip3 install requests ; echo '[?] Done [?]'")

#----------------------------------------------

try:
  import ipapi
except:
  os.system(Fore.RED+"clear ; echo '[!] installing ipapi [!]' ; pip3 install ipapi ; echo '[?] Done [?]'")

#-----------------------------------------------

try:
  import builtwith
except:
  os.system(Fore.RED+"clear ; echo'[!] installing builtwith [!]' ; pip3 install builtwith ; echo '[?] Done [?]'")
banner = (Fore.RED+"""
  _____ __          ___   _______ __  __
 |  _ \| |          | |  |  ____| \ \ / /
 | |_) | | __ _  ___| | _| |__ ___ \ V /  [v0.0] </Beta>
 |  _ <| |/ _` |/ __| |/ |  __/ _ \ > < 
 | |_) | | (_| | (__|   <| | | (_) / . \ 
 |____/|_|\__,_|\___|_|\_|_|  \___/_/ \_\ blackfox-ctrl4.github.io/BlackFOXtool
                                         
""")

menu = (Fore.GREEN+"""Tools :
[01] veiw source of website     [06] Text Encryption
[02] ip and hostname            [07] Generate passlist
[03] whois                      [08] sqlmap
[04] ip whois                   [000] about
[05] port scaner                [/] wiki
[00] exit                       
[#] update                      
""")
toolsSelect = ""
while toolsSelect != "00":
  print(banner + menu)
  toolsSelect = str(input(Fore.CYAN+" ┌─["+Fore.LIGHTCYAN_EX+"BlackFox"+Fore.CYAN+"""]
 └──╼ """+Fore.WHITE+"$ ").lower())

  if(toolsSelect == "1"):
    site = input(Fore.YELLOW+"Enter the address of the site you want to scrap (format example : https://www.google.com) :\n"+"[+] Back "+'\n'+Fore.CYAN+" ┌─["+Fore.LIGHTCYAN_EX+"BlackFox/veiw-source"+Fore.CYAN+"""]
 └──╼ """+Fore.WHITE+"$ ").lower()
    if(site == "00"):
      print(Fore.RED+"[!]"+ "Exiting..."+Fore.RED+"[!]")
      exit(0)
    res = requests.post(site)
    f = open("source.txt", "x")
    f.write(res.text)
    print("The source code of", site, "is written to source.txt\n")
    f.close()

  if(toolsSelect == "2"):
    inpu = input(Fore.YELLOW+"Enter To see : \n[*] ip-hostname"+'\n'+"[1] help"+'\n'+"[00] exit"+'\n'+Fore.CYAN+" ┌─["+Fore.LIGHTCYAN_EX+"BlackFox/ip-hostname"+Fore.CYAN+"""]
 └──╼ """+Fore.WHITE+"$ ").lower()
    if(inpu == "00"):
      print(Fore.RED+"[!]"+ "Exiting..."+Fore.RED+"[!]")
      exit(0)
    elif (inpu == "1"):
      print("")
    elif(inpu == "*"):
      hostname = socket.gethostname()
      IPAddr = socket.gethostbyname(hostname)
      print(Fore.BLUE+"""Hostname :""", hostname, """
IP Adress :""", IPAddr)
      time.sleep(3)
  if(toolsSelect == "3"):
    urlWhois = input(Fore.YELLOW+"Enter the url : "+'\n'+Fore.CYAN+" ┌─["+Fore.LIGHTCYAN_EX+"BlackFox/whois"+Fore.CYAN+"""]
 └──╼ """+Fore.WHITE+"$ ").lower()
    os.system("clear ; whois"+" "+urlWhois)
    time.sleep(3)
  if(toolsSelect == "4"):
    os.system("python3 IpInfo.py")

  if(toolsSelect == "5"):
    ipsc = input(Fore.YELLOW+"Enter the ip :"+'\n'+Fore.CYAN+" ┌─["+Fore.LIGHTCYAN_EX+"BlackFox/port-scanner"+Fore.CYAN+"""]
 └──╼ """+Fore.WHITE+"$ ").lower()
    if(ipsc== "00"):
      print(Fore.RED+"[!]"+ "Exiting..."+Fore.RED+"[!]")
      exit(0)
    ran = input(Fore.YELLOW+"Enter the range : "+'\n'+Fore.CYAN+" ┌─["+Fore.LIGHTCYAN_EX+"BlackFox/port-scanner/range"+Fore.CYAN+"""]
 └──╼ """+Fore.WHITE+"$ ").lower()    
    if(ran == "00"):
      print(Fore.RED+"[!]"+ "Exiting..."+Fore.RED+"[!]")
      exit(0)
    os.system("clear ; python3 port-scanner.py"+ " "+ipsc+" "+ran)

  if(toolsSelect == "6"):
    fin = open("pass.txt", "a")
    passfile = dict()
    password = input(Fore.YELLOW+"Enter the text : "+'\n'+Fore.CYAN+" ┌─["+Fore.LIGHTCYAN_EX+"BlackFox/Text-Encryption"+Fore.CYAN+"""]
 └──╼ """+Fore.WHITE+"$ ").lower()
    if(password == "exit"):
      print(Fore.RED+"[!]"+ "Exiting..."+Fore.RED+"[!]")
      exit(0)
    keypassfile = str(password)
    p = hashlib.sha256()
    p.update(password.encode("utf-8"))
    p_256 = p.hexdigest()
    passfile[keypassfile] = str(p_256)
    fin.write(str(passfile))
    fin.write('\n')
    print(p_256)
    print(passfile)
    time.sleep(3)

  if toolsSelect == '7':
        pchoice = ''
        while pchoice != '0':
            pchoice = str(input(" \n [1] Generate passlist (cupp)\n [2] Generate passlist (Bopscrk)\n [0] Back\n"+'\n'+Fore.CYAN+" ┌─["+Fore.LIGHTCYAN_EX+"BlackFox/Generate-passlist"+Fore.CYAN+"""]
 └──╼ """+Fore.WHITE+"$ ").lower())

            while pchoice != '0':

                cuchoice = ''
                if pchoice == '1':
                    while cuchoice != '0':
                        cuchoice = str(input("\n [1] Generate passlist\n [2] Improve existing passlist\n [3] Download huge passlists from repository\n [0] Back\n"+'\n'+Fore.CYAN+" ┌─["+Fore.LIGHTCYAN_EX+"BlackFox/cupp"+Fore.CYAN+"""]
 └──╼ """+Fore.WHITE+"$ ").lower())

                        if cuchoice == '1':
                            os.system("python3 cupp.py -i")
                        elif cuchoice == '2':       
                            imchoice = str(input("\n Enter the path to your passlist\n"+'\n'+Fore.CYAN+" ┌─["+Fore.LIGHTCYAN_EX+"BlackFox/cupp"+Fore.CYAN+"""]
 └──╼ """+Fore.WHITE+"$ ").lower())
                            plpathc = ("python3 cupp.py -w " + imchoice) 
                            os.system(plpathc)
                        elif cuchoice == '3':
                            os.system("python3 cupp.py -l")
                        elif cuchoice != '0':
                            print("\n Wrong input, Try again.\n"+'\n'+Fore.CYAN+" ┌─["+Fore.LIGHTCYAN_EX+"BlackFox/cupp"+Fore.CYAN+"""]
 └──╼ """+Fore.WHITE+"$ ").lower()
                        


                elif pchoice == '2':
                    os.system("python3 bopscrk.py")

                elif pchoice != '0':
                    print(" \n Wrong input, Try again.\n"+Fore.CYAN+" ┌─["+Fore.LIGHTCYAN_EX+"BlackFox/bopscrk"+Fore.CYAN+"""]
 └──╼ """+Fore.WHITE+"$ ").lower()            
                break
  if(toolsSelect == "00"):
   print(Fore.RED+"[!]"+ "Exiting..."+Fore.RED+"[!]")
   exit(0)

  if(toolsSelect == "000"):
    helpMessage = """BlackFOX is a Script with bunch of tools for hacking
and pentesting.
written with python3
Developers : KerNix3
github : github.com/blackfox-Ctrl4
website : blackfox-ctrl4.github.io/blackFOXtool
email : psyrens@protonmail.com
--------------------------------
[install libraries and setup] --> bash install.sh
[update] --> bash update.sh"""
    print(helpMessage)
    time.sleep(2)
    sd = input(" \n"+'\n'+Fore.CYAN+" ┌─["+Fore.LIGHTCYAN_EX+"BlackFox/about"+Fore.CYAN+"""]
 └──╼ """+Fore.WHITE+"$ ").lower()
    if(sd == "00"):
      print(Fore.RED+"[!]"+ "Exiting..."+Fore.RED+"[!]")
      exit(0)
  if(toolsSelect == "10"):
   url = input("Enter the url : ")
   if(url == "00"):
     print(Fore.RED+"[!]"+ "Exiting..."+Fore.RED+"[!]")
     exit(0)
   os.system("cd sqlmap ; python3 sqlmap.py -u"+'"'+url+'"')
  if(toolsSelect == "/"):
     wikiQ = input("[1] Website <wiki> \n"+"[2] github <wiki>"+'\n'+Fore.CYAN+" ┌─["+Fore.LIGHTCYAN_EX+"BlackFox/about"+Fore.CYAN+"""]
 └──╼ """+Fore.WHITE+"$ ").lower()
     if(wikiQ == "1"):
        websiteHelpMessageWiki = "opening websit wiki ..."
        print(Fore.RED+websiteHelpMessageWiki)
        time.sleep(3)
        wiki = "https://blackfox-ctrl4.github.io/BlackFOXtool/"
        webbrowser.open_new_tab(wiki)
     if(wikiQ == "2"):
       githubHelpMessage = "opening github wiki ..."
       print(Fore.RED+githubHelpMessage)
       time.sleep(3)
       githubWiki = "https://www.github.com/blackfox-Ctrl4/BlackFOXtool"
       webbrowser.open_new_tab(githubWiki)
     if(wikiQ == "00"):
        print(Fore.RED+"[!]"+ "Exiting..."+Fore.RED+"[!]")
        exit(0)