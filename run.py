#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : Fake-information
# @url    : http://github.com/MasterBurnt
# @author : MasterBurnt 


#Library
try:
    import urllib.request 
    from os import system 
    from time import sleep, time
except ImportError as e:
    print(e)

#Colors
c1 = '\033[0m'  #white
c2 = '\033[92m' #green
c3 = '\033[96m' #cyan
c4 = '\033[91m' #red
c5 = '\033[93m' #yellow 
c6 = '\033[94m' #blue 
c7 = '\033[90m' #Black 

#Banner
def banner():
    system('clear')
    banner = c2+f"""
                      . 
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
                   {c4}F4k3 !nf0rm47!0n
                   

          {c6}url {c7}:{c3} http://github.com/MasterBurnt
                 {c6}author {c7}:{c3} MasterBurnt  
                   """
    return print(banner)

#Format
def format(x):
    json = "https://randomuser.me/api/?format=json"
    csv = "https://randomuser.me/api/?format=csv"
    yaml = "https://randomuser.me/api/?format=yaml"
    xml = "https://randomuser.me/api/?format=xml"
    
    if x == "1":
        return json
    elif x == "2":
       return csv 
    elif x == "3":
        return yaml
    elif x == "4":
        return xml 
    elif x == "0":        
        print(c2+f'[*] {c6}B{c2}e{c3}s{c4}t{c5} {c6}w{c1}i{c2}s{c3}h{c4}e{c5}s{c7} =)')
        sleep(3)
        system('clear')
        exit(0)
    else:
        print(c4+f'[!]{c7} Please do not specify an out-of-range option!')
        sleep(2)
        Feature()
#Feature
def Feature():
    while True:
        banner()
        up = f"""
{c2}[1]{c1} Get fake information file {c7}:{c1} format-Json
{c2}[2]{c1} Get fake information file {c7}:{c1} format-Csv
{c2}[3]{c1} Get fake information file {c7}:{c1} format-Yaml
{c2}[4]{c1} Get fake information file {c7}:{c1} format-Xml
{c2}[0]{c1} Exit! 
 """
        for i in up:
             print(i,end='')
             sleep(0.003)
        call = input(c2+f"\n[?]{c1} Please select an option {c7}:{c5} ").strip()
        if call not in ["1","2","3","4","0"]:
            print(c4+f'[-] {c1}Out-of-bounds option! ')
            sleep(2)
            pass
        else:
            return format(call)
            break    

#Request & Saved
def output():
        url = Feature()
        try:
            r = urllib.request.urlopen(url).read().decode()
        except :
            print(c7+f"\n[!] {c4}Please check your connection to the Internet! ")
            exit(1)
            
        File_Extension = url[34:] 
        file = open(f"fakeinfo.{File_Extension}", "wt")
        file.write(r)
        file.close()
        print(c2+f"[+]{c1} file saved {c7}:{c1} fakeinfo.{File_Extension}")
        sleep(2)
        return output()
            
#Run                 
if __name__ == '__main__':
    output()

