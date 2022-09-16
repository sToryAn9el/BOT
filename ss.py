import os
import requests
from bs4 import BeautifulSoup as bs
from colorama import init, Fore, Style
from concurrent.futures import ThreadPoolExecutor

try:
	os.mkdir('Checker') #outputresult
except:
    pass

s = requests.Session()
uagent = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36'} #useragent

os.system('cls' if os.name == 'nt' else 'clear') #clearterminal

init()
merah = Fore.RED #color
hijau = Fore.GREEN #color
cyan = Fore.CYAN #color
kuning = Fore.YELLOW #color
reset = Fore.RESET #color
cerah = Style.BRIGHT #bright

def shell(domain):
    try:
        site = domain.replace("https://", "").replace("http://","").replace("\n","")
    except:
        pass
    req = s.get('http://' + site, headers=uagent, timeout=20).text
    if "Owner/Group" in req:
        print(f'[{cerah+hijau}#{reset}] '+site+f' | {cerah+hijau}200{reset}')
        with open('Checker/results.txt', 'a+') as f:
            f.write('http://' + site + "\n")
    elif "Permission" in req:
        print(f'[{cerah+hijau}#{reset}] '+site+f' | {cerah+hijau}200{reset}')
        with open('Checker/results.txt', 'a+') as f:
            f.write('http://' + site + "\n")
    elif "&nbsp;UPLOAD" in req:
        print(f'[{cerah+hijau}#{reset}] '+site+f' | {cerah+hijau}200{reset}')
        with open('Checker/results.txt', 'a+') as f:
            f.write('http://' + site + "\n")
    elif "Software" in req:
        print(f'[{cerah+hijau}#{reset}] '+site+f' | {cerah+hijau}200{reset}')
        with open('Checker/results.txt', 'a+') as f:
            f.write('http://' + site + "\n")
    elif "[ SIZE ]" in req:
        print(f'[{cerah+hijau}#{reset}] '+site+f' | {cerah+hijau}200{reset}')
        with open('Checker/results.txt', 'a+') as f:
            f.write('http://' + site + "\n")
    elif "[ PERM ]" in req:
        print(f'[{cerah+hijau}#{reset}] '+site+f' | {cerah+hijau}200{reset}')
        with open('Checker/results.txt', 'a+') as f:
            f.write('http://' + site + "\n")
    else:
        print(f'[{cerah+hijau}#{reset}] '+site+f' | {merah}ERROR{reset}')

banner =f"""
{hijau} ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ 
{hijau}||S |||H |||E |||L |||L |||S |||C |||A |||N |||S ||  {reset} Author  : ./sTory An9el
{hijau}||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||  {reset} Version : 1.0
{hijau}|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|  {reset} Telegam : @seothief
"""
if __name__ == '__main__':
    try:
        print(banner)
        site = input('[?] Shells List > ') #domainlist
        perline = open(site,'r').read().splitlines()
        print('')
        with ThreadPoolExecutor(max_workers=int(10)) as e:
            [e.submit(shell, i) for i in perline]
    except KeyboardInterrupt:
        print(f'\n\n{merah}[!] {reset}CTRL + C DETECT {merah}[!]') #forkeyboardinterrupt
    except:
        print(f'\n{merah}[!] {reset}INCORRECT {merah}[!]')
