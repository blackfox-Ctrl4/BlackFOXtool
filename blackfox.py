import bs4
import requests
import socket
from warnings import filterwarnings
from ipwhois import IPWhois
import time
import hashlib
import os
print("""
  _____ __          ___   _______ __  __
 |  _ \| |          | |  |  ____| \ \ / /
 | |_) | | __ _  ___| | _| |__ ___ \ V /  v 0.0
 |  _ <| |/ _` |/ __| |/ |  __/ _ \ > < Beta
 | |_) | | (_| | (__|   <| | | (_) / . \ 
 |____/|_|\__,_|\___|_|\_|_|  \___/_/ \_\
                                         
""")

x = ("""Tools :
[1] veiw source of website     [6] sha256
[2] ip and hostname            [7] encryptm
[3] whois                      [8] password list(cupp)
[4] ip whois                   [9] password list(Bopscrk)
[5] scan host                  [10] SQL map
[exit] exit                    [about] about
""")

print(x)

toolsSelect = input(">>>")

if(toolsSelect == "1"):
  while True:
   site = input("Enter the address of the site you want to scrap (format example : https://www.google.com) :")
   if(site == "exit"):
     print("exiting...")
     exit(0)
   res = requests.post(str(site))
   f = open("source.txt", "x")
   f.write(res.text)
   f.close()

if(toolsSelect == "2"):
  while True:
    inpu = input("Enter : ")
    if(inpu == "exit"):
      print("exiting...")
      exit(0)
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("""Hostname :""", hostname, """
IP Adress :""", IPAddr)

if(toolsSelect == "3"):
  while True:
    url = str(input("Enter The address of site (format example : https://www.google.com) :"))
    if(url == "exit"):
      print("exitig...")
      exit(0)

if(toolsSelect == "4"):
  os.system("python3 IpInfo.py")

if(toolsSelect == "5"):
  while True:
    from socket import *
    startTime = time.time()

    if __name__ == '__main__':
      target = input('Enter the host to be scanned: ')
      if(target == "exit"):
        print("exit ...")
        exit(0)
      t_IP = gethostbyname(target)
      print ('Starting scan on host: ', t_IP)
   
    for i in range(50, 500):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
         print ('Port %d: OPEN' % (i,))
      s.close()
    print('Time taken:', time.time() - startTime)

if(toolsSelect == "6"):
  while True:
    fin = open("pass.txt", "a")
    passfile = dict()
    password = input("Enter : ")
    if(password == "exit"):
      print("exiting...")
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

if(toolsSelect == "7"):
  result = ""
  message = ""
  choice = ""
  while choice != 0:
    choice = input("""Encryption [1]\nDecryption [2]\nExit [0]\n$""")

    if(choice == "1"):
      message = input("Enter The text to Encrypt : ")
      if(message == "exit"):
        print("exiting...")
        exit(0)
      for i in range(0, len(message)):
        result = result + chr(ord(message[i]) - 13)
      print(result + "\n")
      result = ""

    elif (choice == "2"):
      message = input("Enter the text to Decrypt : ")
      if(message == "exit"):
        print("exiting...")
        exit(0)
      for i in range(0, len(message)):
        result = result + chr(ord(message[i]) + 13 )
        print(result + "\n")
      
    elif (choice == "0" or "exit"):
      print("exiting...")
      exit(0)

if(toolsSelect == "exit"):
  print("exiting.....")
  exit(0)

if(toolsSelect == "about"):
  while True:
    helpMessage = """BlackFOX is a Script with bunch of tools for hacking
and pentesting.
written with python3
Developers : KerNix3 & FOX1EN
github : github.com/blackfox-Ctrl4
website : blackfox-ctrl4.github.io/blackFOXtool
email : psyrens@protonmail.com
--------------------------------
[install libraries and setup] --> bash install.sh
[update] --> bash update.sh"""
    print(helpMessage)
    time.sleep(2)
    sd = input("$")
    if(sd == "exit"):
      print("exiting...")
      exit(0)
    if(sd == "programmer"):
      print("""===============
      KerNix3 & FOX1EN
      ===============
      psyrens@protonmail.com
    ===============""")
    time.sleep(3)

if(toolsSelect == "8"):
  os.system('python3 cupp.py -i')
if(toolsSelect == "9"):
  os.system("python3 bopscrk.py -i")
if(toolsSelect == "10"):
  url = input("Enter the url : ")
  os.system("cd sqlmap ; python3 sqlmap.py -u"+'"'+url+'"')