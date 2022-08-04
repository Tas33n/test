import telebot, requests, random, json, time
from time import sleep
from telebot.async_telebot import AsyncTeleBot
from telebot import types
from requests.structures import CaseInsensitiveDict
token = "5555959023:AAGAB3clPrA"

bot = telebot.TeleBot(token)

rules = str("""
The rules for ZERO2 4 CIRCLE SUPPORT♥️ are:

⚠️READ THE RULES CAREFULLY!⚠️

if you do not follow the rules you will be permanently ban from this group ✅

(1) Don't Use 18+ Words 🔞
(2) Don't Forward Messages From Others Channels Or With Group/Channel Tags 🚫
(3) Don't Use Any Slang Words 🚫
(4) Don't Spam To The Group 🚫
(5) Self promote not allowed 🚫
(6) Don't mention your channel 🚫
""")
@bot.message_handler(content_types=["new_chat_members"])

def wlc(message):
  uname = str(message.from_user.first_name)
  bot.reply_to(message, "Hey there "+uname+"! \nWeclome to INFO CIRCLE 🌺\n"+rules,reply_markup=markup)


markup=types.InlineKeyboardMarkup()
button=types.InlineKeyboardButton('CHANNEL',url="https://t.me/DCBD04")
button2=types.InlineKeyboardButton('ADMIN',url="https://t.me/AKXVAU")
button3=types.InlineKeyboardButton('SUPPORT GROUP',url="https://t.me/zero2_group")
markup.add(button,button2)
markup.add(button3)
#start
@bot.message_handler(commands=['start'])
def send_welcome(message):
  uname = str(message.from_user.first_name)
  bot.reply_to(message, "Hey there "+uname+"!!\nWelcome to ZERO2 4 CIRCLE bot 🌺.\n", reply_markup=markup)

@bot.message_handler(commands=['rules'])
def send_rules(message):
  uname = str(message.from_user.first_name)
  bot.reply_to(message, "Hey there "+uname+"🌺.\n"+rules, reply_markup=markup)


@bot.message_handler(commands=['admin'])
def send_admin(message):
  uname = str(message.from_user.first_name)
  bot.reply_to(message, "Hey there "+uname+"🌺.\nClick the buttons bellow for contact with bot Admin.", reply_markup=markup)
  
    
#info_bot
@bot.message_handler(commands=['info'])
def send_info(message):
	bot.reply_to(message, "🔰BOT FEATURES🔰\n\n[01] CIRCLE ID TO INFORMATION ✅\n[02] CIRCLE NUMBER TO INFORMATION ✅\n[03] API BASED IP INFORMATION ✅\n[04] URL SHORTENER ✅\nADMIN : @AKXVAU\nJOIN OUR CHANNEL : @DCBD04", reply_markup=markup)
	
	
#ID
@bot.message_handler(commands=['id'])
def send_id(message):
  uid = str("YOUR ID IS : "+str(message.from_user.id))
  bot.reply_to(message, uid, reply_markup=markup)

#help
@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "JOIN OUR CHANNER AND GROUP !", reply_markup=markup)

#status
@bot.message_handler(commands=['status'])
def send_status(message):
	bot.reply_to(message, "I AM ALWAYS ACTIVE BUDDY!", reply_markup=markup)


#circle	
@bot.message_handler(commands=['circle'])
def send_circle(message):
  m = str(message.text)
  if m == "":
    bot.reply_to(message, "INVALID ID OR NUMBER\nTYPE /circle YOUR ID OR NUMBER", reply_markup=markup)
  elif m == "/circle":
    bot.reply_to(message, "INVALID ID OR NUMBER\nTYPE /circle YOUR ID OR NUMBER", reply_markup=markup)
  elif m == "/circle@zero4circle_bot":
    bot.reply_to(message, "INVALID ID OR NUMBER\nTYPE /circle YOUR ID OR NUMBER", reply_markup=markup)
  else:
    fmsg = m.replace("/circle ", "")
    api = str("https://redthryssa.xyz/circle.php?id="+fmsg)
    bot.reply_to(message, "PLEASE WAIT ....\n")
  req = requests.get(api).text
  x = json.loads(str(req))
  success = (x["rdesc"])
  if success != "OK":
    error = str("DATA NOT FOUND !\nERROR CODE : "+req)
    bot.reply_to(message, error)
    
    
  data=(x["data"])
  number1 =(data["msisdn"])
  nickname1 =(data["nickname"])
  name1 =(data["name"])
  point1=(data["points"])
  follower1=(data["followers"])
  following1=(data["following"])
  friend1=(data["friends"])
  birthday1 = (data["birthday"])
  mlstatus1 = (data["mlstatus"])
  sd1 = (data["start_date"])
  
  #data_as_value
  name = str('Name : '+name1)
  nickname = str('Nickname : '+nickname1)
  number = str('Number : '+number1)
  friends = str('Friends : '+friend1)
  following = str('Following : '+following1)
  follower = str('Followers : '+follower1)
  point = str('Points : '+point1)
  birthday = str('Date Of Birth : '+birthday1)
  mlstatus = str('Mlstatus : '+mlstatus1)
  start = str('Start Date : '+sd1)
  my = "JOIN OUR OFFICIAL CHANNEL : @DCBD04\nADMIN : @AKXVAU ♥️"
  time.sleep(2)
  bot.reply_to(message,name+"\n"+nickname+"\n"+number+"\n"+birthday+"\n"+point+"\n"+friends+"\n"+follower+"\n"+following+"\n"+mlstatus+"\n"+start+"\n\n\n"+my, reply_markup=markup)
  """
@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, "I DON'T UNDERSTAND THAT WHAT ARE YOU SAYING.\nPLEASE CONTACT WITH @AKXVAU ♥️", reply_markup=markup)
  """

@bot.message_handler(commands=['ip'])
def send_ip(message):
  m = str(message.text)
  if m == "":
    bot.reply_to(message, "INVALID OPTION\nTYPE /ip IP-ADDRESS", reply_markup=markup)
  elif m == "/ip":
    bot.reply_to(message, "INVALID OPTION\nTYPE /ip IP-ADDRESS", reply_markup=markup)
  elif m == "/ip@zero4circle_bot":
    bot.reply_to(message, "INVALID OPTION\nTYPE /ip IP-ADDRESS", reply_markup=markup)
  else:
    fmsg = m.replace("/ip ", "")
    api = str("http://ip-api.com/json/"+fmsg)
    bot.reply_to(message, "PLEASE WAIT ....\n")
  req = requests.get(api).text
  x = json.loads(str(req))
  status = (x["status"])
  ip1 = (x["query"])
  country1 = (x["country"])
  cc1 = (x["countryCode"])
  region1 = (x["region"])
  city1 = (x["city"])
  zip1 = (x["zip"])
  tz1 = (x["timezone"])
  isp1 = (x["isp"])
  org1 = (x["org"])
  as1 = (x["as"])
  ip = str('IP : '+ip1)
  country = str('Country : '+country1)
  cc = str('Country Code : '+cc1)
  region = str('Region : '+region1)
  city = str('City : '+city1)
  zipx = str('Zip : '+zip1)
  tz = str('Time-Zone : '+tz1)
  org = str('Oeg : '+org1)
  isp = str('Isp : '+isp1)
  asx = str('AS : '+as1)
  if status != "success":
    bot.reply_to(message, "FAILED TO COLLECT INFORMATION.....\n")
  else:
    bot.reply_to(message,ip+"\n"+country+"\n"+cc+"\n"+region+"\n"+city+"\n"+tz+"\n"+zipx+"\n"+isp+"\n"+org+"\n"+asx+"\n\n\nAPI BASED RESULTS ✅", reply_markup=markup)

@bot.message_handler(commands=['short'])
def send_ip(message):
  m = str(message.text)
  if m == "":
    bot.reply_to(message, "INVALID OPTION\nTYPE /short LONG URL", reply_markup=markup)
  elif m == "/short":
    bot.reply_to(message, "INVALID OPTION\nTYPE /short LONG URL", reply_markup=markup)
  elif m == "/short@zero4circle_bot":
    bot.reply_to(message, "INVALID OPTION\nTYPE /short LONG URL", reply_markup=markup)
  else:
    fmsg = m.replace("/short ", "")
    api = str("https://is.gd/create.php?format=simple&url="+fmsg)
    urlurl = "http://tinyurl.com/api-create.php"
    headersurl = CaseInsensitiveDict()
    headersurl["Content-Type"] = "application/json"
    dataurl = '{"url": "'+fmsg+'"}'
    bot.reply_to(message, "PLEASE WAIT ....\n")
    api2 = str("https://v.gd/create.php?format=simple&url="+fmsg)
    
  req = requests.get(api).text
  req2= requests.post(urlurl, headers=headersurl, data=dataurl).text
  req3 = requests.get(api2).text
  url1 = str("URL1 : "+req)
  url2 = str("URL2 : "+req2)
  url3 = str("URL3 : "+req3)
  bot.reply_to(message,url1+"\n"+url2+"\n"+url3+"\n\n\nAPI BASED RESULTS ✅", reply_markup=markup)
  
bot.infinity_polling()
