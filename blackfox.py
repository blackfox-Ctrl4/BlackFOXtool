import bs4
import requests
import socket
from warnings import filterwarnings
from ipwhois import IPWhois
import time
import hashlib
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
[3] whois                      [8]
[4] ip whois                   [9]
[5] scan host                  [10]
* <exit> = exit *              * <help> = help *
""")

print(x)

toolsSelect = input(">>>")

if(toolsSelect == "1"):
  while True:
   site = input("Enter the address of the site you want to scrap (format example : https://www.google.com) :")
   if(site == "exit"):
     print("exit ...")
     exit(0)
   res = requests.post(str(site))
   f = open("source.txt", "x")
   f.write(res.text)
   f.close()

if(toolsSelect == "2"):
  while True:
    inpu = input("Enter : ")
    if(inpu == "exit"):
      print("exit ...")
      exit(0)
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("""Hostname :""", hostname, """
IP Adress :""", IPAddr)

if(toolsSelect == "3"):
  while True:
    url = str(input("Enter The address of site (format example : https://www.google.com) :"))
    if(url == "exit"):
      print("exit ...")
      exit(0)

if(toolsSelect == "4"):
  while True:
    ip = input("Enter the ip address :")
    obj = IPWhois(ip)
    find = obj.lookup_whois()
    print(find)

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
      print("exit ...")
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
    choice = input("""Encryption [1]\nDecryption [2]\nExit [0]\n>>>""")

    if(choice == "1"):
      message = input("Enter The text to Encrypt : ")
      if(message == "exit"):
        print("exit ...")
        exit(0)
      for i in range(0, len(message)):
        result = result + chr(ord(message[i]) - 13)
      print(result + "\n")
      result = ""

    elif (choice == "2"):
      message = input("Enter the text to Decrypt : ")
      if(message == "exit"):
        print("exit ...")
        exit(0)
      for i in range(0, len(message)):
        result = result + chr(ord(message[i]) + 13 )
        print(result + "\n")
      
    elif (choice == "0" or "exit"):
      print("exit ...")
      exit(0)

if(toolsSelect == "exit"):
  print("exit .....")
  exit(0)

if(toolsSelect == "help"):
  while True:
    helpMessage = """BlackFOX <tools for hacking>
write on <python3>
programmer <KerNix3>
type <basic>
website <blackfox.github.com>
email <blackfox@protonmail.com>
------------------------------
[install libarays] <bash install.sh>
[update tool] <bash update.sh>
[1] veiw source of website <Enter 1 | Enter The Website | go to source.txt | for exit [exit]>
[2] your ip and hostname <Enter 2 | Enter again | for exit [exit]>
[3] whois for doamins <Enter 3 | Enter the website | for exit [exit]"""
    print(helpMessage)
    sd = input(">>>")
    if(sd == "exit"):
      print("exit ...")
      exit(0)