#!/usr/bin/env python3
# Author: @haithamaouati
# Version:1.0

import argparse
import colorama
import os
import requests
import time

from colorama import Fore, Back, Style
colorama.init()

os.system('cls' if os.name == 'nt' else 'clear')

print('''\

  _._     _,-'""`-._
 (,-.`._,'(       |\`-/|
     `-.-' \ )-`( , o o)
           `-    \`_`"'-
''')

print(' Author: ' + Fore.CYAN + '@haithamaouati' + Fore.WHITE + ' Version: ' + Fore.YELLOW + '1.0\n' + Fore.WHITE)
print(' A simple admin panel finder tool\n')

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', metavar='<url>', type=str, help='URL website (e.g. http://127.0.0.1/)')
parser.add_argument('-w', '--wordlist', metavar='<wordlist>', type=str, help='Wordlist file (e.g. wordlist.txt)')

args = parser.parse_args()

if args.url == None or args.wordlist == None:
	parser.print_help()
	exit();
url = args.url
wordlist = args.wordlist

with open(wordlist,'r') as list:
  for i in list:
    time.sleep(1)
    x = i.rstrip('\n')
    check = requests.get(url + x)
    try:
      if check.status_code == 200:
        with open("result.txt",'a') as result:
          result.write(url + x +"\n")
        print(Fore.GREEN + '[+] ' + Fore.WHITE + url + x + Fore.GREEN + ' [200]')
        print(Fore.GREEN + '[*] ' + Fore.WHITE + 'Saved to: ' + Fore.YELLOW + 'result.txt')
        result.close()
      else:
        print(Fore.RED + '[-] ' + Fore.WHITE + url + x + Fore.RED + ' [404]')
    except ValueError:
      print(Fore.RED + '[!] ' + Fore.WHITE + 'Something wrong')