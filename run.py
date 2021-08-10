#!/usr/bin/env python3

import requests
from colorama import Fore,init 
import os 
import time

init() 
os.system("clear")

# api
api = 'https://randomuser.me/api'

# 200
response = requests.get(api)
out = response.json()

#StatusLocation
status = True

#copyright 
def copyright():
    print(Fore.GREEN+"""

                      00
                      000
                     00000                  .
                     000000                00
      .             0000000              0000
      0000          0000000            00000
      00000         00000000          000000
       000000       00000000        0000000
        0000000     00000000      000000000
        0000000      0000000     000000000
         0000000     00000000   000000000
           000000000  0000000   00000000
             0000000   000000  0000000            .
              000000  00000  0000000        000000
   .           000000  0000  000000    000000000
    0000000     000000 000   0000   00000000000
     0000000000   0000  00  0000  00000000000
       00000000000  000 00 000  0000000000
          00000000000 00 0 0  000000000
             00000000000000 0000
                      000000000
                    000     000000
""")
    print(f"""                  F4k3 !nf0rm47!0n{Fore.WHITE} 
                     Written by{Fore.RED}\n                    Master Burnt\n\n            {Fore.CYAN}    Telegram : @MrBurnt""")


# output
def output():
    print(Fore.YELLOW+"""
____ ____ _  _ ____    _ _  _ ____ ____
|___ |__| |_/  |___    | |\ | |___ |  |
|    |  | | \_ |___    | | \| |    |__|
""") 

    print(Fore.GREEN+f"┌─[First and last name ~@Fake information]") 
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["name"]["first"]," "+out["results"][0]["name"]["last"] )  
    print(Fore.GREEN+"┌─[dob-date ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["dob"]["date"])
    print(Fore.GREEN+"┌─[dob-age ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["dob"]["age"])
    print(Fore.GREEN+"┌─[Gender ~@Fake information]") 
    print("└──╼ 卐"+Fore.WHITE,out["results"][0]["gender"])
    print(Fore.GREEN+"┌─[Title ~@Fake information]" )
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["name"]["title"])
    print(Fore.GREEN+"┌─[StreetNumber ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE,out["results"][0]["location"]["street"]["number"])
    print(Fore.GREEN+"┌─[StreetName ~@Fake information]") 
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["location"]["street"]["name"])
    print(Fore.GREEN+"┌─[City ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["location"]["city"])
    print(Fore.GREEN+"┌─[State ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["location"]["state"])
    print(Fore.GREEN+"┌─[Country ~@Fake information]") 
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["location"]["country"])
    print(Fore.GREEN+"┌─[PostCode ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["location"]["postcode"])
    print(Fore.GREEN+"┌─[Coordinates-Latitude ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["location"]["coordinates"]["latitude"])
    print(Fore.GREEN+"┌─[Coordinates-Longitude ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["location"]["coordinates"]["longitude"])
    print(Fore.GREEN+"┌─[Timezone-Offset ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["location"]["timezone"]["offset"])
    print(Fore.GREEN+"┌─[Timezone-Description ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["location"]["timezone"]["description"])    
    print(Fore.GREEN+"┌─[Phone ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["phone"])
    print(Fore.GREEN+"┌─[Cell ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["cell"])
    print(Fore.GREEN+"┌─[id-name ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["id"]["name"])
    print(Fore.GREEN+"┌─[id-value ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["id"]["value"])
    print(Fore.GREEN+"┌─[Photo-large link ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["picture"]["large"])
    print(Fore.GREEN+"┌─[Photo-medium link ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["picture"]["medium"])
    print(Fore.GREEN+"┌─[Photo-large link ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["picture"]["large"])
    print(Fore.GREEN+"┌─[Photo-thumbnail link ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["picture"]["thumbnail"])  
    print(Fore.GREEN+"┌─[Email ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["email"]) 
    print(Fore.GREEN+"┌─[Login-Uuid ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["login"]["uuid"])
    print(Fore.GREEN+"┌─[Login-Username ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["login"]["username"])
    print(Fore.GREEN+"┌─[Login-Password ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["login"]["password"])
    print(Fore.GREEN+"┌─[Login-Salt ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["login"]["salt"])
    print(Fore.GREEN+"┌─[Login-md5 ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["login"]["md5"])
    print(Fore.GREEN+"┌─[Login-sha1 ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["login"]["sha1"])
    print(Fore.GREEN+"┌─[Login-sha256 ~@Fake information]")
    print("└──╼ 卐"+Fore.WHITE, out["results"][0]["login"]["sha256"]) 
    
    print(Fore.CYAN+" \n Information received =|\n")

   

    

while status:
    goal = input(f"""{Fore.YELLOW}
____ ____ _  _ ____    _ _  _ ____ ____
|___ |__| |_/  |___    | |\ | |___ |  |
|    |  | | \_ |___    | | \| |    |__|
{Fore.CYAN}
[1] Get fake information
[2] Written by . . .
[3] Exit
{Fore.GREEN}
┌─[option ~@Fake information]
└──╼ 卐 [+] ~>{Fore.WHITE}""" )
    if goal == "1":
        os.system("clear")
        break 
        
    elif goal == "2":
        os.system("clear")
        copyright()
        time.sleep(5)
        os.system("clear")
            
    elif goal == "3":
        os.system("clear")
        print(Fore.RED+"  .::Best wishes!::. ")
        time.sleep(1)
        os.system("clear") 
        exit(0)
        
    else:
        os.system("clear")
        print(Fore.RED+"You only have two options: 1 or 2 or 3!Try again!" )
        time.sleep(3)
        os.system("clear")
   
output()

while status:
        coun = input(Fore.GREEN+f"""
┌─[~$Fake information]
└──╼ 卐{Fore.WHITE}[1] New fake information! 
       [2] Exit!{Fore.GREEN} 
┌─[~$Fake information]
└──╼ 卐[+] ~> {Fore.WHITE}""")

        if coun == "1":
            os.system("clear")
            # api
            api = 'https://randomuser.me/api'
            # 200
            response = requests.get(api)
            out = response.json()
            output()
            continue 
            
        elif coun == "2":
            os.system("clear")
            print(Fore.RED+"  .::Best wishes!::. ")
            time.sleep(1)
            os.system("clear")
            exit(0)
            
        else:
            os.system("clear")
            print(Fore.RED+"You only have two options: 1 or 2!Try again! " )
            time.sleep(3)
            os.system("clear")

