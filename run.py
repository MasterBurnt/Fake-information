#!/usr/bin/env python3

import requests
from colorama import Fore,init 
import os 
import time

init()
c1 = Fore.WHITE
c2 = Fore.GREEN
c3 = Fore.RED
c4 = Fore.CYAN
c5 = Fore.YELLOW


# api
api = 'https://randomuser.me/api'

# 200
try:
    response = requests.get(api)
    out = response.json()
except:
    print(c2+f'Check your {c3}connection {c2}to the {c3}Internet!')
    exit(1)
os.system('clear')
#StatusLocation
status = True

#copyright 
def copyright():
    print(c2+"""
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
    print(f"""                  F4k3 !nf0rm47!0n{c1} 
                     Written by{c3}\n                    Master Burnt\n\n            {c4}    Telegram : @MrBurnt""")


# output
def output():
    print(c5+"""
____ ____ _  _ ____    _ _  _ ____ ____
|___ |__| |_/  |___    | |\ | |___ |  |
|    |  | | \_ |___    | | \| |    |__|
""") 

    print(c2+f"┌─[First and last name ~@Fake information]") 
    print("└──╼ "+c1, out["results"][0]["name"]["first"]," "+out["results"][0]["name"]["last"] )  
    print(c2+"┌─[dob-date ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["dob"]["date"])
    print(c2+"┌─[dob-age ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["dob"]["age"])
    print(c2+"┌─[Gender ~@Fake information]") 
    print("└──╼ "+c1,out["results"][0]["gender"])
    print(c2+"┌─[Title ~@Fake information]" )
    print("└──╼ "+c1, out["results"][0]["name"]["title"])
    print(c2+"┌─[StreetNumber ~@Fake information]")
    print("└──╼ "+c1,out["results"][0]["location"]["street"]["number"])
    print(c2+"┌─[StreetName ~@Fake information]") 
    print("└──╼ "+c1, out["results"][0]["location"]["street"]["name"])
    print(c2+"┌─[City ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["location"]["city"])
    print(c2+"┌─[State ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["location"]["state"])
    print(c2+"┌─[Country ~@Fake information]") 
    print("└──╼ "+c1, out["results"][0]["location"]["country"])
    print(c2+"┌─[PostCode ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["location"]["postcode"])
    print(c2+"┌─[Coordinates-Latitude ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["location"]["coordinates"]["latitude"])
    print(c2+"┌─[Coordinates-Longitude ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["location"]["coordinates"]["longitude"])
    print(c2+"┌─[Timezone-Offset ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["location"]["timezone"]["offset"])
    print(c2+"┌─[Timezone-Description ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["location"]["timezone"]["description"])    
    print(c2+"┌─[Phone ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["phone"])
    print(c2+"┌─[Cell ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["cell"])
    print(c2+"┌─[id-name ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["id"]["name"])
    print(c2+"┌─[id-value ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["id"]["value"])
    print(c2+"┌─[Photo-large link ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["picture"]["large"])
    print(c2+"┌─[Photo-medium link ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["picture"]["medium"])
    print(c2+"┌─[Photo-large link ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["picture"]["large"])
    print(c2+"┌─[Photo-thumbnail link ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["picture"]["thumbnail"])  
    print(c2+"┌─[Email ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["email"]) 
    print(c2+"┌─[Login-Uuid ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["login"]["uuid"])
    print(c2+"┌─[Login-Username ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["login"]["username"])
    print(c2+"┌─[Login-Password ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["login"]["password"])
    print(c2+"┌─[Login-Salt ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["login"]["salt"])
    print(c2+"┌─[Login-md5 ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["login"]["md5"])
    print(c2+"┌─[Login-sha1 ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["login"]["sha1"])
    print(c2+"┌─[Login-sha256 ~@Fake information]")
    print("└──╼ "+c1, out["results"][0]["login"]["sha256"]) 
    
    print(c4+" \n Information received =|\n")

   

    

while status:
    goal = input(f"""{c2}
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
                    000     000000 {c3}

                   F4k3 !nf0rm47!0n
                    
{c4}
[1] Get fake information
[2] Written by . . .
[3] Exit
{c2}
┌─[option ~@Fake information]
└──╼  [+] ~>{c1}""" )
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
        print(c3+"  .::Best wishes!::. ")
        time.sleep(1)
        os.system("clear") 
        exit(0)
        
    else:
        os.system("clear")
        print(c3+"You only have two options: 1 or 2 or 3!Try again!" )
        time.sleep(3)
        os.system("clear")
   
output()

while status:
        coun = input(c2+f"""
┌─[~$Fake information]
└──╼ {c1}[1] New fake information! 
     [2] Exit!{c2} 
┌─[~$Fake information]
└──╼ [+] ~> {c1}""")

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
            print(c3+"  .::Best wishes!::. ")
            time.sleep(1)
            os.system("clear")
            exit(0)
            
        else:
            os.system("clear")
            print(c3+"You only have two options: 1 or 2!Try again! " )
            time.sleep(3)
            os.system("clear")
 
