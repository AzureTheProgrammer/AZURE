import requests, hashlib, os, time, binascii, json, uuid
from requests_html import HTMLSession

session = HTMLSession()

def program():
    os.system('cls')

    print("""
     █████╗     ███████╗    ██╗   ██╗    ██████╗     ███████╗
    ██╔══██╗    ╚══███╔╝    ██║   ██║    ██╔══██╗    ██╔════╝
    ███████║      ███╔╝     ██║   ██║    ██████╔╝    █████╗  
    ██╔══██║     ███╔╝      ██║   ██║    ██╔══██╗    ██╔══╝  
    ██║  ██║    ███████╗    ╚██████╔╝    ██║  ██║    ███████╗
    ╚═╝  ╚═╝    ╚══════╝     ╚═════╝     ╚═╝  ╚═╝    ╚══════╝""")
    print("Welcome!")
    print("")
    print("Please choose from one of the options of what you want to do!")
    print("")
    print("1. Grab Proxies (SSL)\n2. Not sure yet\n3. Track an IP\n4. Log Out")
    print("")
    choice = input(">> ")

    # Grab Proxies
    if choice == "1":
        os.system('cls')

        print("""
         █████╗     ███████╗    ██╗   ██╗    ██████╗     ███████╗
        ██╔══██╗    ╚══███╔╝    ██║   ██║    ██╔══██╗    ██╔════╝
        ███████║      ███╔╝     ██║   ██║    ██████╔╝    █████╗  
        ██╔══██║     ███╔╝      ██║   ██║    ██╔══██╗    ██╔══╝  
        ██║  ██║    ███████╗    ╚██████╔╝    ██║  ██║    ███████╗
        ╚═╝  ╚═╝    ╚══════╝     ╚═════╝     ╚═╝  ╚═╝    ╚══════╝""")
        
        i = 1
        
        r = session.get('https://www.sslproxies.org/')

        proxies = list(zip(r.html.xpath('//*[@id="proxylisttable"]/tbody/tr/td[1]/text()'),r.html.xpath('//*[@id="proxylisttable"]/tbody/tr/td[2]/text()')))

        input("The Script is ready to run! Press Enter to start")
        
        for proxy in proxies:
            r = requests.get('https://extreme-ip-lookup.com/json/' + proxy[0])
            proxy_data = r.json()
            proxy_location = proxy_data["country"]

            print(f"{i} Gathered Proxy: " + proxy[0] + ":" + proxy[1] + " (" + proxy_location + ")")
            i = i + 1
            f = open('proxies.txt', 'a+')
            f.write(proxy[0] + ":" + proxy[1] + "\n")
            f.close()

        print("")
        print("Can't find anymore proxies!")
        print("Proxies have been moved to a text file 'proxies.txt'!")
        print("Proxies can be used for option 2")
        print("Taking you back to the menu!")
        time.sleep(10)
        program()

    # Not sure yet
    if choice == "2":
        os.system('cls')

    # Track an IP
    if choice == "3":
        os.system('cls')
        print("""
         █████╗     ███████╗    ██╗   ██╗    ██████╗     ███████╗
        ██╔══██╗    ╚══███╔╝    ██║   ██║    ██╔══██╗    ██╔════╝
        ███████║      ███╔╝     ██║   ██║    ██████╔╝    █████╗  
        ██╔══██║     ███╔╝      ██║   ██║    ██╔══██╗    ██╔══╝  
        ██║  ██║    ███████╗    ╚██████╔╝    ██║  ██║    ███████╗
        ╚═╝  ╚═╝    ╚══════╝     ╚═════╝     ╚═╝  ╚═╝    ╚══════╝""")

        print("Please enter the IP to track below!")
        print("")
        ip = input("IP: ")
        r = requests.get('https://extreme-ip-lookup.com/json/' + ip)
        data = r.json()
        
        print("")
        print("CITY: " + data["city"])
        print("CONTINENT: " + data["continent"])
        print("COUNTRY: " + data["country"])
        print("REGION: " + data["region"])
        print("HOSTNAME: " + data["ipName"])
        print("ISP: " + data["isp"])
        print("ORG: " + data["org"])
        print("IP: " + data["query"])
        print("")
        
        input("Press Enter to return to the menu!")
        program()

    # Log out
    if choice == "4":
        print("Logging out...")
        time.sleep(2)
        login()
    

def login():
    os.system('cls')
        
    print("""
     █████╗     ███████╗    ██╗   ██╗    ██████╗     ███████╗
    ██╔══██╗    ╚══███╔╝    ██║   ██║    ██╔══██╗    ██╔════╝
    ███████║      ███╔╝     ██║   ██║    ██████╔╝    █████╗  
    ██╔══██║     ███╔╝      ██║   ██║    ██╔══██╗    ██╔══╝  
    ██║  ██║    ███████╗    ╚██████╔╝    ██║  ██║    ███████╗
    ╚═╝  ╚═╝    ╚══════╝     ╚═════╝     ╚═╝  ╚═╝    ╚══════╝""")
    print("")
    print("Please login with your registered username!")
    username = input("Username: ")
    password = input("Password: ")
    mac_address = hex(uuid.getnode())

    # Creating the Hash
    print("Creating the hash...")
    hash_username = hashlib.pbkdf2_hmac('sha256', bytes(username, 'utf-8'), b'salt', 150000)
    hash_password = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), b'salt', 150000)
    hash_mac = hashlib.pbkdf2_hmac('sha256', bytes(mac_address, 'utf-8'), b'salt', 150000)
    
    user_hex = binascii.hexlify(hash_username)
    pass_hex = binascii.hexlify(hash_password)
    mac_hex = binascii.hexlify(hash_mac)
    
    the_hash = user_hex + pass_hex + mac_hex
    print("Hash Created!")

    #Checking the database
    print("Checking to see if you are in the database...")
    database = requests.get('http://xsecurity.000webhostapp.com/app/database.txt')
    time.sleep(3)

    if the_hash in database.content:
        os.system('cls')
        print(f"[LOGGED IN] Welcome, {username}!")
        print("Redirecting you to the program...")
        time.sleep(4)
        program()
    else:
        os.system('cls')
        print("Can't find a user with this hash!")
        print("If the error continues, please get in contact with the owner!")
        time.sleep(3)
        login()

login()
